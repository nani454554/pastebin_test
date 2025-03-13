from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_snippet():
    response = client.post("/snippets/", json={"content": "Hello, world!", "is_public": True})
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_nonexistent_snippet():
    response = client.get("/snippets/nonexistent")
    assert response.status_code == 404
