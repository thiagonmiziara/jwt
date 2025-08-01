import unittest
from unittest.mock import Mock
from src.controllers.balance_editor import BalanceEditorController
from src.models.interface.user_repository import UserRepositoryInterface


class TestBalanceEditorController(unittest.TestCase):

    def setUp(self):
        self.mock_user_repository = Mock(spec=UserRepositoryInterface)
        self.controller = BalanceEditorController(self.mock_user_repository)

    def test_edit_balance_success(self):
        user_id = 1
        new_balance = 100.50

        expected_response = {"type": "User", "count": 1, "new_balance": new_balance}

        response = self.controller.edit(user_id, new_balance)

        self.mock_user_repository.edit_balance.assert_called_once_with(
            user_id, new_balance
        )
        self.assertEqual(response, expected_response)
