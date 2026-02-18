# Python Games API

A simple FastAPI application for Python games and utilities.

## Setup

```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

## Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check

## Testing

```bash
pytest tests/
```
