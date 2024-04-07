from application.contracts.products.filter_products_request import FilterProductsRequest
from domain.product.gender_values import Gender
from infrastructure.persistence.models.additional_for_product_models import (
    ProductColorOrm,
    ProductSizeOrm,
)
from infrastructure.persistence.models.brand_models import BrandOrm
from infrastructure.persistence.models.category_models import CategoryOrm
from infrastructure.persistence.models.product_models import ProductImageOrm, ProductOrm
from infrastructure.persistence.repositories.mappers.product_mappers import (
    from_orm_to_catalog_product,
    from_orm_to_product,
)
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import and_, or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from web_api.exc.brand_exc import BrandNotFound
from web_api.exc.product_exc import (
    CategoryNotFound,
    ProductAlreadyExist,
    ProductNotFound,
)


class ProductRepository(BaseRepository):
    def get_products_models(self):
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

    async def get_prices(self) -> list[int]:
        query = select(ProductOrm.price)
        result = await self.db.execute(query)
        prices = result.scalars().all()

        return prices

    async def get_all_images(self):
        query = select(ProductImageOrm)
        images = await self.db.execute(query)
        images = images.scalars().all()

        return images

    async def add_image(self, product_id: int, filename: str):
        product = await self.db.get(ProductOrm, product_id)

        image = ProductImageOrm(image=filename, product_id=product_id, product=product)

        self.db.add(image)
        await self.db.flush()
        await self.db.commit()

        return f"Successfully uploaded {filename} for {product.name}"

    async def get_image(self, id: int):
        return await self.db.get(ProductImageOrm, id)

    async def add_product(self, data: dict) -> None:
        category = await self.db.get(CategoryOrm, data["category_id"])
        if category is None:
            raise CategoryNotFound()

        brand = await self.db.get(BrandOrm, data["brand_id"])
        if brand is None:
            raise BrandNotFound()

        try:
            product = ProductOrm(**data, category=category, brand=brand)

            self.db.add(product)
            await self.db.commit()
        except IntegrityError:
            raise ProductAlreadyExist()

    async def get_product(self, id: int):
        query = self.get_products_models()
        query = query.filter(ProductOrm.id == id)

        product = await self.db.execute(query)
        product = product.unique().scalars().first()

        if product is None:
            raise ProductNotFound()

        return from_orm_to_product(product)

    async def get_filtered_products(self, data: FilterProductsRequest):
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

        query = select(ProductOrm, ProductImageOrm, ProductSizeOrm)
        query = query.join(ProductImageOrm)
        query = query.filter(ProductOrm.price <= price)

        if genders:
            query = query.filter(or_(ProductOrm.gender.in_(genders), ProductOrm.gender == Gender.unisex))

        if brands:
            query = query.join(BrandOrm).filter(BrandOrm.name.in_(brands))

        if colors:
            query = query.join(ProductColorOrm).filter(ProductColorOrm.name.in_(colors))

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
            joinedload(ProductOrm.images),
            joinedload(ProductOrm.sizes),
        )

        unique_products = await self.db.execute(query)
        unique_products = unique_products.unique().scalars().all()

        if order_by[0] == "-":
            unique_products = unique_products[::-1]

        return [from_orm_to_catalog_product(product) for product in unique_products]

    async def get_all_products(self):
        query = self.get_products_models()

        result = await self.db.execute(query)
        product_models = result.unique().scalars().all()

        return product_models

    async def get_populars(self):
        query = self.get_products_models()
        query = query.order_by(ProductOrm.quantity_sold.desc())

        result = await self.db.execute(query)
        product_models = result.unique().scalars().all()

        return [from_orm_to_catalog_product(product) for product in product_models]

    async def get_new_arrivals(self):
        query = self.get_products_models()

        query = query.order_by(ProductOrm.created.desc())

        result = await self.db.execute(query)
        product_models = result.unique().scalars().all()

        return [from_orm_to_catalog_product(product) for product in product_models]

    async def get_colors(self, name: str):
        query = self.get_products_models()

        query = query.filter(ProductOrm.name == name)

        result = await self.db.execute(query)
        product_models = result.unique().scalars().all()

        return [from_orm_to_catalog_product(product) for product in product_models]
