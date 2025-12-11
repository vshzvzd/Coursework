import pytest
from app import app, db
from models import User, InventoryItem, InventoryCheck, InventoryCheckDetail, LogEntry

@pytest.fixture(scope="module")
def test_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope="module")
def new_user():
    return User(first_name="Иван", last_name="Иванов", role="Заведующий хоз. частью", login="ivan", password="1234")

def test_user_creation(test_app, new_user):
    db.session.add(new_user)
    db.session.commit()
    assert new_user.id is not None
    assert new_user.role == "Заведующий хоз. частью"

def test_inventory_item_creation(test_app):
    item = InventoryItem(name="Компьютер", category="Техника", cost=50000, status="В эксплуатации")
    db.session.add(item)
    db.session.commit()
    assert item.id is not None
    assert item.status == "В эксплуатации"

def test_inventory_check_creation(test_app, new_user):
    db.session.add(new_user)
    db.session.commit()
    check = InventoryCheck(responsible_user_id=new_user.id)
    db.session.add(check)
    db.session.commit()
    assert check.id is not None
    assert check.responsible_user_id == new_user.id

def test_log_entry_creation(test_app, new_user):
    db.session.add(new_user)
    db.session.commit()
    log = LogEntry(user_id=new_user.id, action="Создание пользователя")
    db.session.add(log)
    db.session.commit()
    assert log.id is not None
    assert log.action == "Создание пользователя"
