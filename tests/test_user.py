import pytest
import time
import uuid
from utils.api_client import post, get, put, delete


@pytest.fixture
def new_user():
    unique_email = f"testuser_{uuid.uuid4()}@example.com"
    payload = {
        "name": "Test User",
        "gender": "male",
        "email": unique_email,
        "status": "active"
    }
    response = post("/users", payload)
    assert response.status_code == 201, f"User creation failed: {response.json()}"
    return response.json()


def test_create_user(new_user):
    assert new_user["name"] == "Test User"


def test_get_user(new_user):
    response = get(f"/users/{new_user['id']}")
    assert response.status_code == 200
    assert response.json()["email"] == new_user["email"]


def test_update_user_name(new_user):
    updated_data = {"name": "Updated Name"}
    response = put(f"/users/{new_user['id']}", updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"


def test_user_duplicate_email(new_user):
    payload = {
        "name": "Another User",
        "gender": "female",
        "email": new_user["email"],  # duplicate
        "status": "active"
    }
    response = post("/users", payload)
    assert response.status_code == 422
    assert any(error["field"] == "email" for error in response.json())


def test_delete_user(new_user):
    response = delete(f"/users/{new_user['id']}")
    assert response.status_code == 204
