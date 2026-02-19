import { useState, useEffect } from 'react'
import './App.css'

interface Issue {
  id?: number
  title: string
  description: string
  status: string
}

const API_BASE_URL = 'http://localhost:8000'

function App() {
  const [issues, setIssues] = useState<Issue[]>([])
  const [formData, setFormData] = useState<Issue>({
    title: '',
    description: '',
    status: 'open'
  })
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchIssues()
  }, [])

  const fetchIssues = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/issues`)
      if (!response.ok) throw new Error('Failed to fetch issues')
      const data = await response.json()
      setIssues(data)
      setError(null)
    } catch (err) {
      setError('Failed to fetch issues. Make sure the backend is running.')
      console.error(err)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    try {
      const response = await fetch(`${API_BASE_URL}/api/issues`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
      if (!response.ok) throw new Error('Failed to create issue')
      await fetchIssues()
      setFormData({ title: '', description: '', status: 'open' })
      setError(null)
    } catch (err) {
      setError('Failed to create issue')
      console.error(err)
    } finally {
      setIsLoading(false)
    }
  }

  const handleDelete = async (id: number) => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/issues/${id}`, {
        method: 'DELETE',
      })
      if (!response.ok) throw new Error('Failed to delete issue')
      await fetchIssues()
      setError(null)
    } catch (err) {
      setError('Failed to delete issue')
      console.error(err)
    }
  }

  const handleStatusChange = async (id: number, newStatus: string) => {
    const issue = issues.find(i => i.id === id)
    if (!issue) return

    try {
      const response = await fetch(`${API_BASE_URL}/api/issues/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ...issue, status: newStatus }),
      })
      if (!response.ok) throw new Error('Failed to update issue')
      await fetchIssues()
      setError(null)
    } catch (err) {
      setError('Failed to update issue')
      console.error(err)
    }
  }

  return (
    <div className="container">
      <header>
        <h1>📋 Project Issue Report</h1>
        <p>Track and manage project issues</p>
      </header>

      {error && (
        <div className="error-banner">
          ⚠️ {error}
        </div>
      )}

      <div className="content">
        <section className="form-section">
          <h2>Create New Issue</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="title">Title</label>
              <input
                type="text"
                id="title"
                value={formData.title}
                onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                required
                placeholder="Enter issue title"
              />
            </div>
            <div className="form-group">
              <label htmlFor="description">Description</label>
              <textarea
                id="description"
                value={formData.description}
                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                required
                placeholder="Enter issue description"
                rows={4}
              />
            </div>
            <div className="form-group">
              <label htmlFor="status">Status</label>
              <select
                id="status"
                value={formData.status}
                onChange={(e) => setFormData({ ...formData, status: e.target.value })}
              >
                <option value="open">Open</option>
                <option value="in-progress">In Progress</option>
                <option value="closed">Closed</option>
              </select>
            </div>
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Creating...' : 'Create Issue'}
            </button>
          </form>
        </section>

        <section className="issues-section">
          <h2>Issues ({issues.length})</h2>
          {issues.length === 0 ? (
            <p className="no-issues">No issues yet. Create one to get started!</p>
          ) : (
            <div className="issues-list">
              {issues.map((issue) => (
                <div key={issue.id} className="issue-card">
                  <div className="issue-header">
                    <h3>{issue.title}</h3>
                    <span className={`status-badge ${issue.status}`}>
                      {issue.status}
                    </span>
                  </div>
                  <p className="issue-description">{issue.description}</p>
                  <div className="issue-actions">
                    <select
                      value={issue.status}
                      onChange={(e) => handleStatusChange(issue.id!, e.target.value)}
                      className="status-select"
                    >
                      <option value="open">Open</option>
                      <option value="in-progress">In Progress</option>
                      <option value="closed">Closed</option>
                    </select>
                    <button
                      onClick={() => handleDelete(issue.id!)}
                      className="delete-button"
                    >
                      🗑️ Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>
      </div>
    </div>
  )
}

export default App
