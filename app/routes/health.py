"""Health check endpoint."""

from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db_session

router = APIRouter(tags=["health"])


async def test_database_connection() -> bool:
    """Test database connectivity by executing a simple query.
    
    Returns:
        bool: True if database is reachable, False otherwise.
    """
    try:
        async with get_db_session() as session:
            await session.execute(text("SELECT 1"))
            return True
    except Exception:
        return False


@router.get("/health")
async def health_check():
    """Return application health status including database connectivity."""
    db_connected = await test_database_connection()
    
    if db_connected:
        return {"status": "healthy", "database": "connected"}
    else:
        return {"status": "degraded", "database": "disconnected"}
