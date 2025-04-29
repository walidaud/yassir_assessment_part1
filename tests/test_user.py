# tests/test_users.py
import pytest
import time
from utils.api_client import post, get

@pytest.fixture
def new_user():
    unique_email = f"testuser_{int(time.time())}@example.com"
    payload = {
        "name": "Test User",
        "gender": "male",
        "email": unique_email,
        "status": "active"
    }
    response = post("/users", payload)
    print(response.json())  # For debugging if needed
    assert response.status_code == 201, f"User creation failed: {response.json()}"
    return response.json()  # Return actual user data

def test_create_user(new_user):
    assert new_user["email"].startswith("testuser_")

def test_get_user(new_user):
    user_id = new_user["id"]
    response = get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id