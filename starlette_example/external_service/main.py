from starlette.applications import Starlette
import uvicorn
from starlette.responses import JSONResponse
from starlette.routing import Route


def some_end_point(request):
    return JSONResponse({"Greeting": 'Hello Denis'})


test_app = Starlette(routes=[Route('/test_app/some_end_point', some_end_point)])


def main() -> None:

    uvicorn.run(
        app="starlette_example.external_service.main:test_app",
        host="0.0.0.0",
        port=8001)