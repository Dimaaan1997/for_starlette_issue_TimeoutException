from starlette.applications import Starlette
import uvicorn
from starlette_example.main_service.client_for_external_service import Client
from starlette.routing import Route
from starlette.responses import PlainTextResponse


def create_string(request):
    client = Client()
    denis_greeting = client.get_denis_greeting()
    return PlainTextResponse('Hello Dima, %s' % denis_greeting)


def create_string_2(request):
    return PlainTextResponse('Hello Dima')


app = Starlette(routes=[Route('/app/hello_people', create_string), Route('/app/hello_people_2', create_string_2)])


def main() -> None:
    uvicorn.run(
        app="starlette_example.main_service.main:app",
        host="0.0.0.0",
        port=8000)
