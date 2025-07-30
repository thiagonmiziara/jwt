from .jwt_handler import JwtHandler


def test_jwt_handler():
    jwt_handler = JwtHandler()
    body = {"username": "John Doe", "age": 38}

    token = jwt_handler.create_jwt_token(body)
    token_information = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_information["username"] == body["username"]
    assert token_information["age"] == body["age"]
