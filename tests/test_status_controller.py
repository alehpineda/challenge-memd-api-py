from fastapi.testclient import TestClient

from app.main import app


# Fastapi test client
client = TestClient(app)


def test_healthcheck():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Member API ready to go!"}
