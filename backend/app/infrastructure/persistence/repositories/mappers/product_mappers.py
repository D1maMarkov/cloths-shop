from domain.product.product import CatalogProduct, Product
from infrastructure.persistence.models.product_models import ProductImageOrm, ProductOrm
from infrastructure.persistence.repositories.mappers.brand_mappers import (
    from_orm_to_brand,
)
from infrastructure.persistence.repositories.mappers.category_mapper import (
    from_orm_to_category,
)
from infrastructure.persistence.repositories.mappers.color_mapper import (
    from_orm_to_color,
)
from infrastructure.persistence.repositories.mappers.size_mapper import (
    from_orm_to_products_sizes,
)
from web_api.config import get_settings


def from_orm_to_image(image: ProductImageOrm) -> str:
    return f"{get_settings().HOST}/products/image/{image.id}"


def from_orm_to_catalog_product(product: ProductOrm) -> CatalogProduct:
    return CatalogProduct(
        id=product.id,
        image=from_orm_to_image(product.images[0]),
        name=product.name,
        description=product.description,
        price=product.price,
        sizes=from_orm_to_products_sizes(product.sizes),
    )


def from_orm_to_product(product: ProductOrm) -> Product:
    return Product(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        code=product.code,
        article=product.article,
        gender=product.gender,
        category=from_orm_to_category(product.category),
        brand=from_orm_to_brand(product.brand),
        color=from_orm_to_color(product.color),
        sizes=from_orm_to_products_sizes(product.sizes),
        images=[from_orm_to_image(image) for image in product.images],
    )
