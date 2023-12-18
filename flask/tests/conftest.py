import pytest
from app import create_app, db
from app.models.models import User
from datetime import datetime

email = 'email.test@email.com'
age = 21
timestamp = datetime.strptime('2023-12-12T14:48:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')

# create a test app and create all tables
@pytest.fixture(scope='session')
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app

@pytest.fixture(scope='session')
def test_client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def new_user():
    user = User(
        email = email,
        age = age,
        timestamp = timestamp
    )
    return user
