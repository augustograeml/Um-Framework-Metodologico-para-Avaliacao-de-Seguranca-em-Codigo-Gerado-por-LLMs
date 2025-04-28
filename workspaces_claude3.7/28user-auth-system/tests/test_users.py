import pytest
from app.users.models import User
from app.users.schemas import UserCreate, UserUpdate
from app.db.database import get_db
from sqlalchemy.orm import Session

@pytest.fixture
def test_user(db: Session):
    user = User(username="testuser", email="test@example.com")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def test_create_user(db: Session):
    user_data = UserCreate(username="newuser", email="new@example.com")
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    assert user.username == "newuser"
    assert user.email == "new@example.com"

def test_update_user(test_user, db: Session):
    update_data = UserUpdate(email="updated@example.com")
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(test_user, key, value)
    db.commit()
    db.refresh(test_user)
    assert test_user.email == "updated@example.com"

def test_delete_user(test_user, db: Session):
    db.delete(test_user)
    db.commit()
    assert db.query(User).filter(User.id == test_user.id).first() is None