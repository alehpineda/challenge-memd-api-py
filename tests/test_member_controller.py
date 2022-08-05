import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.controllers.member_controller import (
    retrieve_member_controller,
    create_primary_member_controller,
    create_dependent_member_controller,
)


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
