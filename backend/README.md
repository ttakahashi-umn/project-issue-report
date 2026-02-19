# Backend - FastAPI

FastAPI backend for the Project Issue Report application.

## Setup

### Prerequisites
- Python 3.14 以上
- [uv](https://docs.astral.sh/uv/)（推奨パッケージマネージャー）

### Installation（uv）

1. 仮想環境の自動作成と依存関係のインストール:
```bash
uv sync
```

開発用依存関係（pytest, ruff など）も含める場合:
```bash
uv sync --extra dev
```

2. 開発サーバーの起動:
```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Running the Application

Start the development server:
```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Interactive API docs (Swagger): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## API Endpoints

### Health Check
- `GET /` - Root endpoint
- `GET /health` - Health check endpoint

### Issues
- `GET /api/issues` - Get all issues
- `POST /api/issues` - Create a new issue
- `GET /api/issues/{issue_id}` - Get a specific issue
- `PUT /api/issues/{issue_id}` - Update an issue
- `DELETE /api/issues/{issue_id}` - Delete an issue

## Development

### Code Quality

Format and lint code:
```bash
uv run ruff check .
uv run ruff format .
```

### Testing

Run tests:
```bash
uv run pytest
```

Run tests with coverage:
```bash
uv run pytest --cov=app --cov-report=html
```

## cc-sdd Development Workflow

This project follows the cc-sdd (Cursor-Centric Software Development) methodology:

1. **Context-Driven Development**: Use AI tools to understand and navigate the codebase
2. **Iterative Refinement**: Make small, incremental changes
3. **Continuous Verification**: Test changes immediately after implementation
4. **Documentation First**: Keep documentation up-to-date with code changes
5. **AI-Assisted Code Review**: Leverage AI for code review and suggestions
