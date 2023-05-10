import httpx
import pytest
from starlette_example.main_service.main import app
from starlette.testclient import TestClient


class ServerClient:

    url = 'http://0.0.0.0:8001/test_app/some_end_point'

    def __init__(self, httpx_mock):
        self.mock_request = httpx_mock

        httpx_mock.add_callback(callback=self.return_denis_name,
                                method="GET",
                                url=self.url)

    @staticmethod
    def return_denis_name(request: httpx.Request):
        return httpx.Response(
            status_code=200,
            json={
                "Greeting": 'Hello Denis'})


@pytest.fixture(autouse=True)
def device_client(httpx_mock):
    yield ServerClient(httpx_mock=httpx_mock)


@pytest.fixture()
def test_client():
    with TestClient(app=app) as client:
        yield client

