# Project Structure

## Organization Philosophy

Monorepo with **backend** and **frontend** at top level; each has its own package manifest and run commands. Backend is one Python package (`app`); frontend is Vite-based React app. Specs and steering live under `.kiro/` and guide new features.

## Directory Patterns

### Backend application
**Location**: `backend/app/`  
**Purpose**: FastAPI app, routes, Pydantic models; future: routers, SQLAlchemy models, services.  
**Example**: `app/main.py` — app instance, CORS, `/api/issues` CRUD and health routes.

### Backend tests
**Location**: `backend/tests/`  
**Purpose**: Pytest tests; mirror `app/` layout when needed.  
**Example**: `tests/test_main.py` — API tests (e.g. httpx against `app.main:app`).

### Frontend source
**Location**: `frontend/src/`  
**Purpose**: Entry (`main.tsx`), `App.tsx`, styles, assets.  
**Example**: Flat structure; add `components/`, `api/`, etc. by feature or type as app grows.

### Specs and steering
**Location**: `.kiro/specs/`, `.kiro/steering/`  
**Purpose**: Spec-driven workflow; steering = project memory (product, tech, structure).  
**Example**: `.kiro/specs/<feature-name>/` contains `spec.json`, `requirements.md`, etc.

## Naming Conventions

- **Backend files**: snake_case (e.g. `main.py`, `issue_router.py`)
- **Backend package**: `app` (single top-level package)
- **Frontend**: PascalCase for components; kebab or Pascal for files as per Vite/React norms
- **Specs**: kebab-case feature names (e.g. `github-issue-comments-report`)

## Import Organization

**Backend**:
```python
# App-internal: from app or relative
from fastapi import FastAPI
from pydantic import BaseModel
# Future: from app.models import Issue
```

**Frontend**: ESM; use path aliases if configured (e.g. `@/` for `src/`).

## Code Organization Principles

- Backend: Keep route handlers thin; move logic to services or domain layer when complexity grows. Use Pydantic for all API boundaries.
- Frontend: Prefer components and hooks; keep API calls in a small set of modules for clarity.
- New features that touch DB or external APIs: align with `.kiro/specs/` and steering (tech.md, structure.md).

---
_Document patterns, not file trees. New files following patterns shouldn't require updates_
