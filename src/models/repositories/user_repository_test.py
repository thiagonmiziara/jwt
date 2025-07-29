from unittest.mock import Mock
from .user_repository import UserRepository


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_registry_user():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    username = "John Doe"
    password = "1223"

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert (
        cursor.execute.call_args[0][0]
        == "INSERT INTO users (username, password, balance) VALUES (?, ?, ?)"
    )
    assert cursor.execute.call_args[0][1] == ("John Doe", "1223", 0)
    mock_connection.commit.assert_called_once()


def test_edit_balance():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    user_id = 1
    balance = 100.0

    repo.edit_balance(user_id, balance)
    cursor = mock_connection.cursor.return_value

    assert cursor.execute.call_args[0][0] == "UPDATE users SET balance = ? WHERE id = ?"
    assert cursor.execute.call_args[0][1] == (100.0, 1)
    mock_connection.commit.assert_called_once()


def test_get_user_by_username():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    username = "John Doe"

    repo.get_user_by_username(username)
    cursor = mock_connection.cursor.return_value

    assert (
        cursor.execute.call_args[0][0]
        == "SELECT id, username, password FROM users WHERE username = ?"
    )
    assert cursor.execute.call_args[0][1] == ("John Doe",)
    cursor.fetchone.assert_called_once()
