from fastapi.testclient import TestClient
from app import app

def test_health():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}

def test_greet():
    client = TestClient(app)
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.json() == {"Message":"Hello mr toast man"}