import pytest
from app import app, db
from models import User

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_get_users(client):
    # Добавим пользователя
    from models import User
    user = User(first_name="Иван", last_name="Иванов", role="Заведующий", login="ivan", password="1234")
    db.session.add(user)
    db.session.commit()

    response = client.get("/users")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["name"] == "Иван Иванов"

def test_get_items_empty(client):
    response = client.get("/items")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 0

def test_get_logs_empty(client):
    response = client.get("/logs")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 0
