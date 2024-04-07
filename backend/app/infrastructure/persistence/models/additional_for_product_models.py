from infrastructure.persistence.database import Model
from infrastructure.persistence.models.models import DataFieldOrm
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class ProductSizeOrm(Model):
    __tablename__ = "product_size"

    id = Column(Integer, primary_key=True)
    size = Column(String)

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("ProductOrm")


class ProductColorOrm(DataFieldOrm):
    __tablename__ = "product_color"

    id = Column(Integer, primary_key=True)
