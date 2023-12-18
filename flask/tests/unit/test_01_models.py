from conftest import email, age, timestamp

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check all fields are defined correctly
    """
    assert new_user.email == email
    assert new_user.age == age
    assert new_user.timestamp == timestamp