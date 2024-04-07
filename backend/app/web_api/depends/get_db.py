from infrastructure.persistence.database import new_session


async def get_db():
    async with new_session() as session:
        yield session
