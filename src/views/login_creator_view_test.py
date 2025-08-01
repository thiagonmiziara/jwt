import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.login_creator_view import LoginCreatorView


class MockController:
    def create(self, username: str, password: str) -> dict:
        return {"username": username, "password": password}


def test_handle_user_login_creator():
    body = {"username": "John Doe", "password": "password"}
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    response = login_creator_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {"data": {"username": "John Doe", "password": "password"}}
    assert response.status_code == 200


def test_handle_user_login_creator_with_validation_error():
    body = {"password": "password"}
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        login_creator_view.handle(request)
