"""FastAPI application entry point."""

from fastapi import FastAPI
from app.routes import health
from app.middleware import RateLimitHeaderMiddleware

app = FastAPI(
    title="Python Games API",
    version="0.1.0",
    description="A simple API for Python games and utilities.",
)

app.add_middleware(RateLimitHeaderMiddleware)

app.include_router(health.router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Python Games API"}