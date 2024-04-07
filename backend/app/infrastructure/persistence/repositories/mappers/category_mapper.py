from domain.category.category import Category
from infrastructure.persistence.models.category_models import CategoryOrm


def from_orm_to_category(category: CategoryOrm) -> Category:
    return Category(
        id=category.id, name=category.name, viewed_name=category.viewed_name, basic_category=category.basic_category
    )
