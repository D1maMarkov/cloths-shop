from dataclasses import dataclass

from domain.category.basic_category_values import BasicCategory
from domain.common.base_data_field import BaseDataField


@dataclass
class Category(BaseDataField):
    basic_category: BasicCategory
