from fastapi import Depends
from infrastructure.persistence.repositories.additional_for_products_repository import (
    AdditionalForProductSRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession
from web_api.depends.get_db import get_db


async def get_repository(db: AsyncSession = Depends(get_db)) -> AdditionalForProductSRepository:
    return AdditionalForProductSRepository(db)
