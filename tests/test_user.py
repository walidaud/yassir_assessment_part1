# tests/test_users.py
import pytest
from utils.api_client import post, get, put, delete

@pytest.fixture
def new_user():
    payload = {
        "name": "Test User",
        "gender": "male",
        "email": "testuseranom@example.com",
        "status": "active"
    }
    response = post("/users", payload)
    assert response.status_code == 201
    return response.json()

def test_create_user(new_user):
    assert new_user["name"] == "Test User"

def test_get_user(new_user):
    user_id = new_user["id"]
    response = get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id

def test_update_user(new_user):
    user_id = new_user["id"]
    payload = {"name": "Updated Name"}
    response = put(f"/users/{user_id}", payload)
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["name"] == "Updated Name"

def test_delete_user(new_user):
    user_id = new_user["id"]
    response = delete(f"/users/{user_id}")
    assert response.status_code == 204

def test_unauthorized_access():
    import requests
    bad_headers = {"Authorization": "Bearer invalidtoken"}
    response = requests.get("https://gorest.co.in/public/v2/users", headers=bad_headers)
    assert response.status_code == 401
