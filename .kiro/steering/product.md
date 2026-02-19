# Product Overview

Full-stack application for managing project issues. Serves teams who need to track issues, update status, and (planned) sync with GitHub Project and generate LLM-summarized reports.

## Core Capabilities

- **Issue CRUD**: Create, read, update, delete issues via REST API and UI
- **API-first**: FastAPI backend with OpenAPI docs; frontend consumes `/api/*`
- **Local + Docker**: Run backend/frontend locally or via docker-compose (PostgreSQL included)
- **Spec-driven growth**: New features follow `.kiro/specs/` (e.g. GitHub comments fetch and report)

## Target Use Cases

- Track project issues with title, description, status
- Integrate with GitHub Project (planned): fetch issue comments, store in DB, later summarize with LLM into reports
- Development and demo with minimal setup (uv + npm, or docker-compose)

## Value Proposition

Single repo with clear backend/frontend split, type-safe API (Pydantic), and a path from in-memory demo to persisted data (PostgreSQL, SQLAlchemy) and external integrations.

---
_Focus on patterns and purpose, not exhaustive feature lists_
