# project-issue-report

A full-stack application for managing project issues, built with FastAPI (Python) backend and React (TypeScript) frontend.

## 🏗️ Project Structure

```
project-issue-report/
├── backend/           # FastAPI Python backend（uv）
│   ├── app/          # Application code
│   ├── tests/        # Backend tests
│   ├── pyproject.toml
│   ├── uv.lock       # 依存関係ロックファイル
│   └── README.md
├── frontend/         # React TypeScript frontend
│   ├── src/         # Source code
│   ├── public/      # Static assets
│   ├── package.json
│   └── README.md
└── README.md        # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.14 以上（バックエンドは [uv](https://docs.astral.sh/uv/) 推奨）
- Node.js 18 or higher
- npm or yarn

### Running the Backend

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at http://localhost:8000

### Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at http://localhost:5173

## 📚 Features

### Backend (FastAPI)
- ✅ RESTful API for issue management
- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ CORS enabled for frontend integration
- ✅ Interactive API documentation (Swagger UI)
- ✅ Type-safe with Pydantic models
- ✅ Unit tests with pytest

### Frontend (React + TypeScript)
- ✅ Modern React with TypeScript
- ✅ Responsive design
- ✅ Real-time issue management
- ✅ Status updates
- ✅ Dark/light mode support
- ✅ Built with Vite for fast development

## 🔧 Development Workflow (cc-sdd)

This project follows the **cc-sdd (Cursor-Centric Software Development)** methodology, which emphasizes:

1. **Context-Driven Development**
   - Use AI coding assistants to understand the codebase
   - Navigate and explore code with AI assistance
   - Generate code snippets and boilerplate

2. **Iterative Refinement**
   - Make small, incremental changes
   - Test each change immediately
   - Refine based on feedback

3. **Continuous Verification**
   - Run tests after every change
   - Validate functionality immediately
   - Use automated checks (linting, type checking)

4. **Documentation First**
   - Keep documentation updated with code
   - Write clear, self-documenting code
   - Add comments for complex logic

5. **AI-Assisted Code Review**
   - Use AI for code review suggestions
   - Get refactoring recommendations
   - Identify potential bugs early

### Development Commands

**Backend:**
```bash
# Run tests
uv run pytest

# Lint and format
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy app/
```

**Frontend:**
```bash
# Run linter
npm run lint

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📖 API Documentation

Once the backend is running, access the interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testing

### Backend Tests
```bash
cd backend
uv run pytest
uv run pytest --cov=app --cov-report=html
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🔐 Security

- CORS configured for local development
- Input validation with Pydantic
- TypeScript for type safety
- No sensitive data in version control

## 🤝 Contributing

1. Make changes in small, focused commits
2. Use AI tools to assist with code quality
3. Test your changes thoroughly
4. Update documentation as needed
5. Follow the cc-sdd methodology

## 📝 License

See [LICENSE](LICENSE) file for details.

## 🛠️ Tech Stack

**Backend:**
- FastAPI
- Python 3.14+
- Pydantic
- Uvicorn
- pytest

**Frontend:**
- React 19
- TypeScript
- Vite
- ESLint

## 🎯 Next Steps

- [ ] Add database integration (PostgreSQL/SQLite)
- [ ] Implement user authentication
- [ ] Add issue comments and attachments
- [ ] Deploy to production
- [ ] Add CI/CD pipeline
- [ ] Implement real-time updates with WebSockets