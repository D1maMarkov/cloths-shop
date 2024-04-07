from application.contracts.common.base_data_add_request import BaseDataFieldAddRequest
from domain.category.basic_category_values import BasicCategory


class AddCategoryRequest(BaseDataFieldAddRequest):
    basic_category: BasicCategory
