# Backend - FastAPI

FastAPI backend for the Project Issue Report application.

## Setup

### Prerequisites
- Python 3.11 or higher
- pip or uv package manager

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

For development dependencies:
```bash
pip install -e ".[dev]"
```

### Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
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
ruff check .
ruff format .
```

### Testing

Run tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app --cov-report=html
```

## cc-sdd Development Workflow

This project follows the cc-sdd (Cursor-Centric Software Development) methodology:

1. **Context-Driven Development**: Use AI tools to understand and navigate the codebase
2. **Iterative Refinement**: Make small, incremental changes
3. **Continuous Verification**: Test changes immediately after implementation
4. **Documentation First**: Keep documentation up-to-date with code changes
5. **AI-Assisted Code Review**: Leverage AI for code review and suggestions
