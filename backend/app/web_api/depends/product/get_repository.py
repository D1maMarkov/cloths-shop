from fastapi import Depends
from infrastructure.persistence.repositories.product_repository import ProductRepository
from sqlalchemy.ext.asyncio import AsyncSession
from web_api.depends.get_db import get_db


def get_repository(db: AsyncSession = Depends(get_db)) -> ProductRepository:
    return ProductRepository(db)
