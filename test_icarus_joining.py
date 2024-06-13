import pytest
from icarus_joining import User, icarus_joining

def test_icarus_joining_success():
    user = User(username="icarus", email="icarus@example.com")
    result = icarus_joining(user)
    assert result == "User joined successfully"

def test_icarus_joining_missing_username():
    user = User(username="", email="icarus@example.com")
    result = icarus_joining(user)
    assert result == "Username and email must not be empty"

def test_icarus_joining_invalid_email():
    user = User(username="icarus", email="icarus_at_example.com")
    result = icarus_joining(user)
    assert result == "Invalid email address"