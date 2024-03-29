from database import Model
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class DataFieldOrm(Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String)
    viewed_name = Column(String)


class CategoryOrm(DataFieldOrm):
    __tablename__ = "categories"

    basic_category = Column(String)
    products = relationship("ProductOrm", back_populates="category")


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
    brand = relationship("BrandOrm")


class User(Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    email = Column(String, unique=True)
    orders = relationship("OrderOrm", back_populates="user")
    is_active = Column(Boolean, default=False)
