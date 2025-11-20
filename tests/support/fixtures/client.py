from pytest import fixture
from starlette.testclient import TestClient

from fizz_buzz.__main__ import AppCreator


@fixture
def client() -> TestClient:
    app_creator = AppCreator()
    app = app_creator.app

    return TestClient(app=app)
