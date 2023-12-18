
def test_route(test_client):
    """
    GIVEN a Flask application
    WHEN a GET request is made to '/'
    THEN check that the response is valid
    """

    response_get = test_client.get('/')
    assert response_get.status_code == 200

    response_post = test_client.post('/')
    assert response_post.status_code == 405