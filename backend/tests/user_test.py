from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register_new_user():
    response = client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "testuser@test.com",
            "password": "testpassword",
            "role_id": 1,
            "is_active": True
        }
    )
    assert response.status_code == 200
    assert "User 'testuser' has been registered successfully!" in str(response.content)


def test_register_existing_user():
    response = client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "testuser@test.com",
            "password": "testpassword",
            "role_id": 1,
            "is_active": True
        }
    )
    assert response.status_code == 400
    assert "Username already registered" in str(response.content)


def test_login_user():
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == 302
    assert "/notes" in response.headers["location"]


def test_login_user_incorrect_credentials():
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401
    assert "Invalid username or password" in str(response.content)


def test_authenticate_user():
    response = client.post(
        "/authenticate",
        data={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == 200
    assert "You have successfully logged in!" in str(response.content)
    assert "authenticated.html" in str(response.template.name)
