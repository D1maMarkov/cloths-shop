from domain.common.base_data_field import BaseDataField
from infrastructure.persistence.models.additional_for_product_models import (
    ProductColorOrm,
)


def from_orm_to_color(color: ProductColorOrm) -> BaseDataField:
    return BaseDataField(id=color.id, name=color.name, viewed_name=color.viewed_name)
