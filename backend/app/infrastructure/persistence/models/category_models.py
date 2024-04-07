from infrastructure.persistence.models.models import DataFieldOrm
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class CategoryOrm(DataFieldOrm):
    __tablename__ = "categories"

    basic_category = Column(String)
    products = relationship("ProductOrm", back_populates="category")
