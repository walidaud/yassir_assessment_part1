# tests/test_users.py
import pytest
from utils.api_client import post, get, put, delete

@pytest.fixture
def new_user():
    payload = {
        "name": "Test User",
        "gender": "male",
        "email": "testuser@example.com",
        "status": "active"
    }
    response = post("/users", payload)
    print(response.json())  # This will print the response body, check for error messages.
    return response

def test_create_user(new_user):
    assert new_user.status_code == 201

def test_get_user(new_user):
    # Assuming `new_user` contains the created user data
    response = get(f"/users/{new_user.json()['id']}")
    assert response.status_code == 200
