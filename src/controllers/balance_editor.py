from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.models.interface.user_repository import UserRepositoryInterface


class BalanceEditorController(BalanceEditorInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__user_repository.edit_balance(user_id, new_balance)
        response = self.__format_response(new_balance)
        return response

    def __format_response(self, new_balance: float) -> dict:
        return {"type": "User", "count": 1, "new_balance": new_balance}
