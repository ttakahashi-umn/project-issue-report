"""
Tests for the FastAPI application
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_and_get_issue():
    """Test creating and retrieving an issue"""
    # Create an issue
    issue_data = {
        "title": "Test Issue",
        "description": "This is a test issue",
        "status": "open"
    }
    response = client.post("/api/issues", json=issue_data)
    assert response.status_code == 200
    created_issue = response.json()
    assert created_issue["title"] == issue_data["title"]
    assert "id" in created_issue
    
    # Get all issues
    response = client.get("/api/issues")
    assert response.status_code == 200
    issues = response.json()
    assert len(issues) >= 1
    assert any(issue["id"] == created_issue["id"] for issue in issues)


def test_get_specific_issue():
    """Test getting a specific issue"""
    # First create an issue
    issue_data = {
        "title": "Specific Test Issue",
        "description": "This is for testing specific retrieval",
        "status": "open"
    }
    response = client.post("/api/issues", json=issue_data)
    created_issue = response.json()
    issue_id = created_issue["id"]
    
    # Get the specific issue
    response = client.get(f"/api/issues/{issue_id}")
    assert response.status_code == 200
    issue = response.json()
    assert issue["id"] == issue_id
    assert issue["title"] == issue_data["title"]


def test_update_issue():
    """Test updating an issue"""
    # Create an issue
    issue_data = {
        "title": "Issue to Update",
        "description": "Original description",
        "status": "open"
    }
    response = client.post("/api/issues", json=issue_data)
    created_issue = response.json()
    issue_id = created_issue["id"]
    
    # Update the issue
    updated_data = {
        "title": "Updated Issue",
        "description": "Updated description",
        "status": "closed"
    }
    response = client.put(f"/api/issues/{issue_id}", json=updated_data)
    assert response.status_code == 200
    updated_issue = response.json()
    assert updated_issue["title"] == updated_data["title"]
    assert updated_issue["status"] == updated_data["status"]


def test_delete_issue():
    """Test deleting an issue"""
    # Create an issue
    issue_data = {
        "title": "Issue to Delete",
        "description": "This will be deleted",
        "status": "open"
    }
    response = client.post("/api/issues", json=issue_data)
    created_issue = response.json()
    issue_id = created_issue["id"]
    
    # Delete the issue
    response = client.delete(f"/api/issues/{issue_id}")
    assert response.status_code == 200
    
    # Verify it's deleted (should not be in the list)
    response = client.get("/api/issues")
    issues = response.json()
    assert not any(issue["id"] == issue_id for issue in issues)
