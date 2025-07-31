import pytest
from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreatorController


mock_username = "John Doe"
password = "password"
hashed_password = PasswordHandler().encrypt_password(password)


class MockUserRepository:
    def get_user_by_username(self, username: str) -> tuple[int, str, str]:
        return (10, username, hashed_password)


def test_create():
    login_creator = LoginCreatorController(MockUserRepository())
    response = login_creator.create(mock_username, password)

    assert response["access"] is True
    assert response["username"] == mock_username
    assert response["token"] is not None


def test_create_with_wrong_password():
    login_creator = LoginCreatorController(MockUserRepository())

    with pytest.raises(Exception):
        login_creator.create(mock_username, "password")
