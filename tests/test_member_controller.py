import pytest
from fastapi.testclient import TestClient

from app.main import app

# Fastapi test client
client = TestClient(app)


# Fixtures
@pytest.fixture()
def test_app():
    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture()
def mock_token():
    return "BEARER_123456789asdfqwerzxcv"
