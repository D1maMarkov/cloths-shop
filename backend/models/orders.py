from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import Integer, String, TIMESTAMP, Column
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Model


class OrderOrm(Model):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    secondname = Column(String)
    adress = Column(String)
    phone = Column(String)
    payment = Column(String)
    delivery = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="orders")
    created = Column(TIMESTAMP, default=datetime.utcnow)
    order_products = relationship("OrderProductOrm", back_populates="order")
    #status = Column(String, default="На складе")

class OrderProductOrm(Model):
    __tablename__ = "order products"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("OrderOrm", back_populates="order_products")

    product_model_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    size = Column(String)