from starlette import status


def test_1(test_client):
    response = test_client.get('/app/hello_people')
    assert response.status_code == status.HTTP_200_OK
    assert response.text == 'Hello Dima, Hello Denis'


# this is new style of test with using "request" method with test client, as you recommended
def test_2(test_client):
    response = test_client.request('GET', '/app/hello_people')
    assert response.status_code == status.HTTP_200_OK
    assert response.text == 'Hello Dima, Hello Denis'
