# See documentation: https://docs.pytest.org/en/7.1.x/
# See documentation: https://flask.palletsprojects.com/en/2.1.x/testing/

"""
Tests are simply functions whose names begin with "test_". Use the normal Python
assert statement to check certain facts. The "client" argument to each test is
populated with a client to a fresh instance of the application.
"""


def test_echo(client):
    test_message = {'test_key': 'test_value'}

    response = client.post('/echo', json=test_message)
    assert response.json == test_message


def test_echo_token(client):
    response = client.post('/echo/foobar')
    assert response.json == {'token': 'foobar'}
