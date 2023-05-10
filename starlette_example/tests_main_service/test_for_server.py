from starlette import status


def test_greetings_new(test_client):

    response = test_client.get('/app/hello_people')
    assert response.status_code == status.HTTP_200_OK
    assert response.text == 'Hello Dima, Hello Denis'
