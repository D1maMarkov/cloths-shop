from infrastructure.persistence.database import Model
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class BrandOrm(Model):
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("ProductOrm", back_populates="brand", lazy="selectin")
    image = relationship("BrandImageOrm", back_populates="brand", lazy="selectin")


class BrandImageOrm(Model):
    __tablename__ = "brand_image"

    id = Column(Integer, primary_key=True)
    image = Column(String)

    brand_id = Column(Integer, ForeignKey("brand.id"))
    brand = relationship("BrandOrm", back_populates="image", lazy="selectin")
