from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_chat():
    client = app.test_client()
    response = client.get("/api/chat")
    data = response.get_json()
    assert data["answer"] == 4
