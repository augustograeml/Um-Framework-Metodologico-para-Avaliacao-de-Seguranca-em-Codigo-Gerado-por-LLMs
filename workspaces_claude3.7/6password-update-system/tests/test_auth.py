from app.auth.password_handler import hash_password
from app.auth.email_verifier import verify_email_exists
from app.database.db_connector import update_user_password
import pytest

@pytest.fixture
def setup_database():
    # Setup code to initialize the database connection and create a test user
    pass

def test_update_password_success(setup_database):
    email = "testuser@example.com"
    new_password = "NewSecurePassword123"
    
    # Assuming the user exists in the database
    assert verify_email_exists(email) is True
    
    # Update the password
    update_user_password(email, hash_password(new_password))
    
    # Verify the password was updated (this would require a function to check the password)
    assert check_password(email, new_password) is True

def test_update_password_user_not_found(setup_database):
    email = "nonexistentuser@example.com"
    new_password = "NewSecurePassword123"
    
    # Verify the user does not exist
    assert verify_email_exists(email) is False
    
    # Attempt to update the password and expect failure
    with pytest.raises(UserNotFoundError):
        update_user_password(email, hash_password(new_password))

def test_update_password_invalid_email(setup_database):
    email = "invalid-email-format"
    new_password = "NewSecurePassword123"
    
    # Verify the email format is invalid
    assert not is_valid_email(email)
    
    # Attempt to update the password and expect failure
    with pytest.raises(InvalidEmailError):
        update_user_password(email, hash_password(new_password))