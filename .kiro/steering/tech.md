# Technology Stack

## Architecture

- **Backend**: FastAPI (async), single-app module under `backend/app/`; CORS for frontend origin
- **Frontend**: React 19 + TypeScript, Vite; talks to backend on port 8000
- **Data**: In-memory for demo; PostgreSQL (docker-compose) + SQLAlchemy/psycopg for persistence when wired

## Core Technologies

- **Backend**: Python 3.14+, FastAPI, Pydantic, Uvicorn
- **Frontend**: React 19, TypeScript, Vite 7.x
- **Package managers**: uv (backend), npm (frontend)

## Key Libraries

- **Backend**: FastAPI, Pydantic, SQLAlchemy, psycopg\[binary\] (PostgreSQL, Apple Silicon–friendly)
- **Frontend**: React, Vite; ESLint + TypeScript for quality

## Development Standards

### Type Safety
- Backend: Pydantic models for request/response; Python 3.14 type hints
- Frontend: TypeScript strict; typed API usage

### Code Quality
- Backend: Ruff (lint + format), line-length 100, target py314
- Frontend: ESLint

### Testing
- Backend: pytest, pytest-asyncio; tests under `backend/tests/`
- Frontend: test script available via npm

## Development Environment

### Required Tools
- Python 3.14+ with uv
- Node.js 18+
- Docker (optional, for PostgreSQL and full stack)

### Common Commands
```bash
# Backend
cd backend && uv sync && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uv run pytest
uv run ruff check . && uv run ruff format .

# Frontend
cd frontend && npm install && npm run dev
npm run lint
npm run build
```

## Key Technical Decisions

- **uv for backend**: Lockfile and fast installs; hatchling build, package `app`
- **Single backend module**: `app/main.py` holds routes and in-memory store; new features can split into routers/models under `app/`
- **PostgreSQL driver**: psycopg\[binary\] for native arm64 wheels on Apple Silicon
- **CORS**: Allow `http://localhost:5173` for local frontend

---
_Document standards and patterns, not every dependency_
