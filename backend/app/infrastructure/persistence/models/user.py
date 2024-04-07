from infrastructure.persistence.database import Model
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    email = Column(String, unique=True)
    orders = relationship("OrderOrm", back_populates="user")
    is_active = Column(Boolean, default=False)
