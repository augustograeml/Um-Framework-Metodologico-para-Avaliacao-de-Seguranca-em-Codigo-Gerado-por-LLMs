import pytest
from app import create_app, db
from app.models import Comment

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Comments' in response.data

def test_submit_comment(client):
    response = client.post('/submit_comment', data={
        'name': 'Test User',
        'content': 'This is a test comment.'
    })
    assert response.status_code == 302  # Redirect after submission
    assert Comment.query.count() == 1
    comment = Comment.query.first()
    assert comment.name == 'Test User'
    assert comment.content == 'This is a test comment.'