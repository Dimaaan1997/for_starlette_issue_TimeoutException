import httpx


class Client:

    def get_denis_greeting(self):
        response = httpx.request('GET', 'http://0.0.0.0:8001/test_app/some_end_point')
        denis_name = response.json()['Greeting']
        return denis_name

