from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_tts():
    client = app.test_client()
    response = client.get("/api/tts")
    data = response.get_json()
    assert data["answer"] == 4
