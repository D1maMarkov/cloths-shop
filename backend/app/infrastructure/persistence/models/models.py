from infrastructure.persistence.database import Model
from sqlalchemy import Column, Integer, String


class DataFieldOrm(Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String)
    viewed_name = Column(String)
