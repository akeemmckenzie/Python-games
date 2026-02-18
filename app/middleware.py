"""FastAPI middleware for adding rate limiting headers."""

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class RateLimitHeaderMiddleware(BaseHTTPMiddleware):
    """Middleware to add X-RateLimit-Remaining header to all responses."""

    async def dispatch(self, request: Request, call_next):
        """Process request and add rate limit header to response."""
        response = await call_next(request)
        response.headers["X-RateLimit-Remaining"] = "100"
        return response