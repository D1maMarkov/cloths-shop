from dataclasses import dataclass

from domain.additional_for_product.size_values import SizeValues


@dataclass
class Size:
    size: SizeValues
