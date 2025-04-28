import pytest

@pytest.fixture(scope='session')
def test_client():
    from app.main import app
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='session')
def init_database():
    from app.db.database import get_db
    db = get_db()
    yield db
    db.close()