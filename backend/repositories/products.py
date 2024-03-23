from models.products import ProductOrm, ProductImageOrm, ProductColorOrm, ProductSizeOrm
from schemas.common import SBaseDataFieldAdd, SFiltered
from utils.get_list_from_json import get_list_from_json
from models.models import CategoryOrm, BrandOrm
from fastapi.responses import FileResponse
from sqlalchemy.orm import joinedload
from schemas.products import SProduct
from sqlalchemy import and_, select, or_
from database import new_session
from fastapi import UploadFile
from settings import settings
import os


class ProductRepository:
    @classmethod
    def get_products_models(cls):
        query = select(ProductOrm, BrandOrm, CategoryOrm, ProductImageOrm, ProductColorOrm, ProductSizeOrm)
        query = query.join(BrandOrm)
        query = query.join(CategoryOrm)
        query = query.join(ProductImageOrm)
        query = query.join(ProductColorOrm)
        query = query.outerjoin(ProductSizeOrm, and_(ProductSizeOrm.product, ProductOrm.sizes == None))
        
        query = query.options(joinedload(ProductOrm.brand),
                            joinedload(ProductOrm.category),
                            joinedload(ProductOrm.images),
                            joinedload(ProductOrm.color),
                            joinedload(ProductOrm.sizes))

        return query
    
    @classmethod
    async def get_price_range(cls) -> list[int]:
        async with new_session() as session:
            query = select(ProductOrm)
            result = await session.execute(query)
            products = result.scalars().all()
            
            min_price = 10 ** 9
            max_price = 0
            
            for product in products:
                if product.price < min_price:
                    min_price = product.price
                if product.price > max_price:
                    max_price = product.price
                    
            return [min_price, max_price]

    @classmethod
    async def get_all_images(cls):
        async with new_session() as session:
            query = select(ProductImageOrm)
            images = await session.execute(query)
            images = images.scalars().all()

            return images

    @classmethod
    async def add_image(cls, product_id: int, file: UploadFile):
        async with new_session() as session:
            contents = file.file.read()
            
            if not os.path.exists(settings.PRODUCTS_PATH):
                os.makedirs(settings.PRODUCTS_PATH)

            with open(settings.PRODUCTS_PATH + file.filename, 'wb') as f:
                f.write(contents)

            file.file.close()
            
            product = await session.get(ProductOrm, product_id)

            image = ProductImageOrm(
                image=file.filename, 
                product_id=product_id, 
                product=product
            )
            
            session.add(image)
            await session.flush()
            await session.commit()

            return {"message": f"Successfully uploaded {file.filename, image.id}"}

    @classmethod
    async def get_image(cls, image_id: int):
        async with new_session() as session:
            query = select(ProductImageOrm)
            images = await session.execute(query)
            images = images.scalars().all()
            
            image = await session.get(ProductImageOrm, image_id)
            
            return FileResponse(settings.PRODUCTS_PATH + image.image)

    @classmethod
    async def add_one_product(cls, data: SBaseDataFieldAdd) -> list[int]:
        async with new_session() as session:
            product_dict = data.model_dump()

            category = await session.get(CategoryOrm, product_dict["category_id"])
            product_dict["category"] = category
            
            brand = await session.get(BrandOrm, product_dict["brand_id"])
            product_dict["brand"] = brand

            product = ProductOrm(**product_dict)
            
            session.add(product)
            await session.flush()
            await session.commit()
                
            return [product.id, category.id, brand.id]

    @classmethod
    async def get_product(cls, id: int) -> SProduct:
        async with new_session() as session:
            query = cls.get_products_models()
            query = query.filter(ProductOrm.id==id)

            unique_product = await session.execute(query)
            unique_product = unique_product.unique().scalars().first()

            product = SProduct(**unique_product.__dict__)

            return product

    @classmethod
    async def get_filtered_products(cls, data: SFiltered) -> list[SProduct]:
        async with new_session() as session:
            genders = get_list_from_json(data.gender)
            categories = get_list_from_json(data.category)
            colors = get_list_from_json(data.color)
            brands = get_list_from_json(data.brand)
            sizes = get_list_from_json(data.size)
            basic_category = data.basicCategory

            price = data.price
            quantity = data.quantity
            page_index = data.pageIndex
            order_by = data.orderBy
            
            query = select(ProductOrm, BrandOrm, CategoryOrm, ProductImageOrm, ProductColorOrm, ProductSizeOrm)
            
            if genders:
                query = query.filter(or_(ProductOrm.gender.in_(genders), ProductOrm.gender=="unisex"))
            
            if brands:
                query = query.join(BrandOrm).filter(BrandOrm.name.in_(brands))
            else:
                query = query.join(BrandOrm)
            
            if colors:
                query = query.join(ProductColorOrm).filter(ProductColorOrm.name.in_(colors))
            else:
                query = query.join(ProductColorOrm)
                
            query = query.join(ProductImageOrm)
            query = query.filter(ProductOrm.price <= price)
            
            if order_by[0] == "-":
                query = query.order_by(order_by[1::])
            else:
                query = query.order_by(order_by)
                
            if sizes:
                query = query.outerjoin(ProductSizeOrm, and_(ProductSizeOrm.product, ProductOrm.sizes == None)).filter(ProductSizeOrm.size.in_(sizes))
            else:
                query = query.outerjoin(ProductSizeOrm, and_(ProductSizeOrm.product, ProductOrm.sizes == None))

            if categories:
                query = query.join(CategoryOrm).filter(CategoryOrm.basic_category==basic_category).filter(CategoryOrm.name.in_(categories))
            else:
                query = query.join(CategoryOrm).filter(CategoryOrm.basic_category==basic_category)
                
            query = query.offset(page_index * quantity).limit(quantity)
            query = query.options(joinedload(ProductOrm.brand),
                                joinedload(ProductOrm.category),
                                joinedload(ProductOrm.images),
                                joinedload(ProductOrm.color),
                                joinedload(ProductOrm.sizes))
            
            unique_products = await session.execute(query)
            unique_products = unique_products.unique().scalars().all()
            
            if order_by[0] == "-":
                unique_products = unique_products[::-1]
            
            products = [SProduct(**product.__dict__) for product in unique_products]

            return products

    @classmethod
    async def get_searched_products(cls, search: str) -> list[SProduct]:
        async with new_session() as session:
            query = cls.get_products_models()

            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            search = search.lower()
            serialized_products = []
            for product in product_models:
                serialized_product = SProduct(**product.__dict__)
                if search in serialized_product.category.name.lower() \
                    or search in serialized_product.category.viewed_name.lower() \
                    or search in serialized_product.name.lower() \
                    or search in serialized_product.description.lower() \
                    or search in serialized_product.brand.name.lower():  
                        serialized_products.append(serialized_product)

            return serialized_products

    @classmethod
    async def get_populars(cls):
        async with new_session() as session:
            query = cls.get_products_models()
            query = query.order_by(ProductOrm.quantity_sold.desc())
            
            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            serialized_products = [SProduct(**product.__dict__) for product in product_models]

            return serialized_products
        
    @classmethod 
    async def get_new_arrivals(cls):
        async with new_session() as session:
            query = cls.get_products_models()
            
            query = query.order_by(ProductOrm.created.desc())
            
            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            serialized_products = [SProduct(**product.__dict__) for product in product_models]

            return serialized_products

    @classmethod 
    async def get_colors(cls, name):
        async with new_session() as session:
            query = cls.get_products_models()

            query = query.filter(ProductOrm.name==name)

            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            serialized_products = [SProduct(**product.__dict__) for product in product_models]

            return serialized_products
#276 245 261