import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock, ANY

from app.main import app

# Fastapi test client
client = TestClient(app)


# Fixtures
@pytest.fixture()
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture()
def mock_token():
    return "BEARER_123456789asdfqwerzxcv"

@pytest.fixture
def mock_retrieve_response():
    json_response = {
    "dependents": [],
    "external_id": 1000,
    "relationship": 18,
    "plancode": "11AA22BB",
    "active": True,
    "first_name": "Alex",
    "last_name": "Test",
    "gender": "M",
    "street_1": "742 Evergreen Terrace",
    "street_2": "APT 123",
    "city": "Springfield",
    "state": "NY",
    "zipcode": "12345",
    "benefit_start": "2022-08-01",
    "dob": "1980-01-01"
}
    return json_response


@patch("app.controllers.member_controller.retrieve_member_service")
def test_retrieve_member_controller_not_found(mock_retrieve_member_service, mock_token):
    headers = {"Authorization": mock_token}
    response = client.get("/retrieve/1000", headers=headers)
    assert response.json() == {'detail': 'Not Found'}
