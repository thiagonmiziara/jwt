from .password_handler import PasswordHandler


def test_encrypt():
    password = "123python"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(password)
    password_checked = password_handler.check_password(password, hashed_password)

    assert password_checked
