from fastapi import Depends
from infrastructure.persistence.repositories.order_repository import OrderRepository
from sqlalchemy.ext.asyncio import AsyncSession
from web_api.depends.get_db import get_db


def get_repository(db: AsyncSession = Depends(get_db)) -> OrderRepository:
    return OrderRepository(db)
