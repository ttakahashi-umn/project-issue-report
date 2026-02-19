"""
FastAPI Backend for Project Issue Reporting
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Project Issue Report API",
    description="API for managing project issues",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthCheck(BaseModel):
    status: str
    message: str


class Issue(BaseModel):
    id: int | None = None
    title: str
    description: str
    status: str = "open"


# In-memory storage for demo purposes
issues_db: list[Issue] = []
issue_counter = 1


@app.get("/", response_model=HealthCheck)
async def root():
    """Root endpoint - health check"""
    return HealthCheck(status="ok", message="Project Issue Report API is running")


@app.get("/health", response_model=HealthCheck)
async def health_check():
    """Health check endpoint"""
    return HealthCheck(status="healthy", message="API is operational")


@app.get("/api/issues", response_model=list[Issue])
async def get_issues():
    """Get all issues"""
    return issues_db


@app.post("/api/issues", response_model=Issue)
async def create_issue(issue: Issue):
    """Create a new issue"""
    global issue_counter
    issue.id = issue_counter
    issue_counter += 1
    issues_db.append(issue)
    return issue


@app.get("/api/issues/{issue_id}", response_model=Issue)
async def get_issue(issue_id: int):
    """Get a specific issue by ID"""
    for issue in issues_db:
        if issue.id == issue_id:
            return issue
    return {"error": "Issue not found"}


@app.put("/api/issues/{issue_id}", response_model=Issue)
async def update_issue(issue_id: int, updated_issue: Issue):
    """Update an existing issue"""
    for idx, issue in enumerate(issues_db):
        if issue.id == issue_id:
            updated_issue.id = issue_id
            issues_db[idx] = updated_issue
            return updated_issue
    return {"error": "Issue not found"}


@app.delete("/api/issues/{issue_id}")
async def delete_issue(issue_id: int):
    """Delete an issue"""
    global issues_db
    issues_db = [issue for issue in issues_db if issue.id != issue_id]
    return {"message": "Issue deleted successfully"}
