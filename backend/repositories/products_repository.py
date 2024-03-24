from database import new_session
from enums import Gender
from models.models import BrandOrm, CategoryOrm
from models.products import ProductColorOrm, ProductImageOrm, ProductOrm, ProductSizeOrm
from schemas.common import SBaseDataFieldAdd, SFiltered
from sqlalchemy import and_, or_, select
from sqlalchemy.orm import joinedload


class ProductRepository:
    @classmethod
    def get_products_models(cls):
        query = select(ProductOrm, BrandOrm, CategoryOrm, ProductImageOrm, ProductColorOrm, ProductSizeOrm)
        query = query.join(BrandOrm)
        query = query.join(CategoryOrm)
        query = query.join(ProductImageOrm)
        query = query.join(ProductColorOrm)
        query = query.outerjoin(ProductSizeOrm, and_(ProductSizeOrm.product, ProductOrm.sizes is None))

        query = query.options(
            joinedload(ProductOrm.brand),
            joinedload(ProductOrm.category),
            joinedload(ProductOrm.images),
            joinedload(ProductOrm.color),
            joinedload(ProductOrm.sizes),
        )

        return query

    @classmethod
    async def get_prices(cls) -> list[int]:
        async with new_session() as session:
            query = select(ProductOrm.price)
            result = await session.execute(query)
            prices = result.scalars().all()

            return prices

    @classmethod
    async def get_all_images(cls):
        async with new_session() as session:
            query = select(ProductImageOrm)
            images = await session.execute(query)
            images = images.scalars().all()

            return images

    @classmethod
    async def add_image(cls, product_id: int, filename: str):
        async with new_session() as session:
            product = await session.get(ProductOrm, product_id)

            image = ProductImageOrm(image=filename, product_id=product_id, product=product)

            session.add(image)
            await session.flush()
            await session.commit()

            return f"Successfully uploaded {filename} for {product.name}"

    @classmethod
    async def get_image(cls, id: int):
        async with new_session() as session:
            image = await session.get(ProductImageOrm, id)

            return image

    @classmethod
    async def add_one_product(cls, data: SBaseDataFieldAdd) -> list[int]:
        async with new_session() as session:
            product_dict = data.model_dump()

            category = await session.get(CategoryOrm, product_dict["category_id"])
            brand = await session.get(BrandOrm, product_dict["brand_id"])

            product = ProductOrm(**product_dict, category=category, brand=brand)

            session.add(product)
            await session.flush()
            await session.commit()

            return [product.id, category.id, brand.id]

    @classmethod
    async def get_product(cls, id: int):
        async with new_session() as session:
            query = cls.get_products_models()
            query = query.filter(ProductOrm.id == id)

            product = await session.execute(query)
            product = product.unique().scalars().first()

            return product

    @classmethod
    async def get_filtered_products(cls, data: SFiltered):
        async with new_session() as session:
            genders = data.gender
            categories = data.category
            colors = data.color
            brands = data.brand
            sizes = data.size
            basic_category = data.basicCategory
            price = data.price
            quantity = data.quantity
            page_index = data.pageIndex
            order_by = data.orderBy

            query = select(ProductOrm, BrandOrm, CategoryOrm, ProductImageOrm, ProductColorOrm, ProductSizeOrm)
            query = query.join(ProductImageOrm)
            query = query.filter(ProductOrm.price <= price)

            if genders:
                query = query.filter(or_(ProductOrm.gender.in_(genders), ProductOrm.gender == Gender.unisex))

            if brands:
                query = query.join(BrandOrm).filter(BrandOrm.name.in_(brands))
            else:
                query = query.join(BrandOrm)

            if colors:
                query = query.join(ProductColorOrm).filter(ProductColorOrm.name.in_(colors))
            else:
                query = query.join(ProductColorOrm)

            if order_by[0] == "-":
                query = query.order_by(order_by[1::])
            else:
                query = query.order_by(order_by)

            if sizes:
                query = query.join(ProductSizeOrm).filter(ProductSizeOrm.size.in_(sizes))
            else:
                query = query.outerjoin(ProductSizeOrm, and_(ProductSizeOrm.product, ProductOrm.sizes is None))

            if categories:
                query = (
                    query.join(CategoryOrm)
                    .filter(CategoryOrm.basic_category == basic_category)
                    .filter(CategoryOrm.name.in_(categories))
                )
            else:
                query = query.join(CategoryOrm).filter(CategoryOrm.basic_category == basic_category)

            query = query.offset(page_index * quantity).limit(quantity)
            query = query.options(
                joinedload(ProductOrm.brand),
                joinedload(ProductOrm.category),
                joinedload(ProductOrm.images),
                joinedload(ProductOrm.color),
                joinedload(ProductOrm.sizes),
            )

            unique_products = await session.execute(query)
            unique_products = unique_products.unique().scalars().all()

            if order_by[0] == "-":
                unique_products = unique_products[::-1]

            return unique_products

    @classmethod
    async def get_all_products(cls):
        async with new_session() as session:
            query = cls.get_products_models()

            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            return product_models

    @classmethod
    async def get_populars(cls):
        async with new_session() as session:
            query = cls.get_products_models()
            query = query.order_by(ProductOrm.quantity_sold.desc())

            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            return product_models

    @classmethod
    async def get_new_arrivals(cls):
        async with new_session() as session:
            query = cls.get_products_models()

            query = query.order_by(ProductOrm.created.desc())

            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            return product_models

    @classmethod
    async def get_colors(cls, name):
        async with new_session() as session:
            query = cls.get_products_models()

            query = query.filter(ProductOrm.name == name)

            result = await session.execute(query)
            product_models = result.unique().scalars().all()

            return product_models


# 276 245 261 253 249 211 201
