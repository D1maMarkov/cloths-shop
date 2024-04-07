from datetime import datetime

from infrastructure.persistence.database import Model
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class ProductOrm(Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created = Column(TIMESTAMP, default=datetime.utcnow)
    description = Column(String)
    price = Column(Integer)
    article = Column(String(6), unique=True)
    code = Column(Integer, unique=True)

    color_id = Column(Integer, ForeignKey("product_color.id"))
    color = relationship("ProductColorOrm")

    gender = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("CategoryOrm", back_populates="products")

    brand_id = Column(Integer, ForeignKey("brand.id"))
    brand = relationship("BrandOrm", back_populates="products", lazy="selectin")

    images = relationship("ProductImageOrm", back_populates="product", lazy="selectin")
    sizes = relationship("ProductSizeOrm", back_populates="product", lazy="selectin")
    order_products = relationship("OrderProductOrm", back_populates="product", lazy="selectin")

    quantity_sold = Column(Integer, default=0)


class ProductImageOrm(Model):
    __tablename__ = "product_image"

    id = Column(Integer, primary_key=True)
    image = Column(String)

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("ProductOrm", back_populates="images", lazy="selectin")
