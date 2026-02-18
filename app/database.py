"""Database connection setup."""

import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://localhost:5432/python_games")

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    """Yield a database session."""
    async with async_session() as session:
        yield session
