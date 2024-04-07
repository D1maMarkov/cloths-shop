from domain.additional_for_product.size_values import SizeValues
from pydantic import BaseModel


class Size(BaseModel):
    product_id: int
    size: SizeValues
