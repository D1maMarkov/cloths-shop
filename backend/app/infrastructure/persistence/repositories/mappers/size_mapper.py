from infrastructure.persistence.models.additional_for_product_models import (
    ProductSizeOrm,
)


def from_orm_to_sizes(sizes: ProductSizeOrm) -> list[str]:
    sizes = [size.size for size in sizes]

    if len(sizes) == 0:
        return ["ONE SIZE"]

    return sizes
