# Frontend - React + TypeScript

React frontend for the Project Issue Report application built with Vite.

## Setup

### Prerequisites
- Node.js 18 or higher
- npm or yarn

### Installation

Install dependencies:
```bash
npm install
```

### Running the Application

Start the development server:
```bash
npm run dev
```

The application will be available at http://localhost:5173

### Building for Production

Build the application:
```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

## Development

### Code Quality

Lint code:
```bash
npm run lint
```

### Project Structure

```
src/
├── App.tsx          # Main application component
├── App.css          # Application styles
├── main.tsx         # Application entry point
└── assets/          # Static assets
```

## Features

- ✅ Create new issues
- ✅ View all issues
- ✅ Update issue status
- ✅ Delete issues
- ✅ Real-time updates from backend
- ✅ Responsive design
- ✅ Dark/light mode support

## API Integration

The frontend connects to the FastAPI backend at `http://localhost:8000`.

Make sure the backend is running before starting the frontend application.

## cc-sdd Development Workflow

This project follows the cc-sdd (Cursor-Centric Software Development) methodology:

1. **Context-Driven Development**: Use AI tools to understand and navigate the codebase
2. **Iterative Refinement**: Make small, incremental changes
3. **Continuous Verification**: Test changes immediately after implementation
4. **Documentation First**: Keep documentation up-to-date with code changes
5. **AI-Assisted Code Review**: Leverage AI for code review and suggestions

### Key Practices

- Use TypeScript for type safety
- Keep components focused and reusable
- Write self-documenting code
- Leverage AI for refactoring suggestions
- Test UI changes visually

---

## React + Vite Technical Details

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

