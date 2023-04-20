from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_note():
    note_data = {
        "title": "Test note",
        "description": "This is a test note"
    }
    response = client.post("/note", json=note_data)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Test note",
        "description": "This is a test note"
    }


def test_get_note():
    note_data = {
        "title": "Test note",
        "description": "This is a test note"
    }
    client.post("/note", json=note_data)
    response = client.get("/note/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Test note",
        "description": "This is a test note"
    }


def test_get_notes():
    note_data = {
        "title": "Test note",
        "description": "This is a test note"
    }
    client.post("/note", json=note_data)
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "title": "Test note",
        "description": "This is a test note"
    }]


def test_update_note():
    note_data = {
        "title": "Test note",
        "description": "This is a test note"
    }
    client.post("/note", json=note_data)
    updated_note_data = {
        "title": "Updated test note",
        "description": "This is an updated test note"
    }
    response = client.put("/note/1", json=updated_note_data)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Updated test note",
        "description": "This is an updated test note"
    }


def test_delete_note():
    note_data = {
        "title": "Test note",
        "description": "This is a test note"
    }
    client.post("/note", json=note_data)
    response = client.delete("/note/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Note with id=1 has been deleted"}
