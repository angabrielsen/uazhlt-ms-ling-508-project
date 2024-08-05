from models.user import *

def test_user_creation():
    user = User('john_doe', 'john@example.com')
    assert user.username == 'john_doe'
    assert user.email == 'john@example.com'

def test_user_str():
    user = User('john_doe', 'john@example.com')
    assert str(user) == 'User(username=john_doe, email=john@example.com)'
