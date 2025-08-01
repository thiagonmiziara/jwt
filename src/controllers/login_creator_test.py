import pytest
from unittest.mock import Mock, patch
from src.drivers.password_handler import PasswordHandler
from src.controllers.login_creator import LoginCreatorController
from src.models.interface.user_repository import UserRepositoryInterface


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
    mock_user_repository = Mock(spec=UserRepositoryInterface)
    mock_user_repository.get_user_by_username.return_value = (
        1,
        "test_user",
        "hashed_password_from_db",
    )

    with patch(
        "src.drivers.password_handler.PasswordHandler.check_password",
        return_value=False,
    ):
        login_creator = LoginCreatorController(mock_user_repository)
        with pytest.raises(Exception, match="Wrong password"):
            login_creator.create("test_user", "wrong_password")
