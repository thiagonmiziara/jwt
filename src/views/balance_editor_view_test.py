import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.balance_editor_view import BalanceEditorView


class MockController:
    def edit(self, user_id: str, new_balance: float) -> dict:
        return {"user_id": user_id, "new_balance": new_balance}


def test_handle_balance_editor():
    body = {"new_balance": 100.1}
    params = {"user_id": "123"}
    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    response = balance_editor_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {"data": {"user_id": "123", "new_balance": 100.1}}
    assert response.status_code == 200


def test_handle_balance_editor_with_validation_error():
    body = {"new_balance": 1}
    request = HttpRequest(body=body)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    with pytest.raises(Exception):
        balance_editor_view.handle(request)
