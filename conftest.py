import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def api_session():
    """Returns a requests Session with shared headers."""
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    yield session
    session.close()

@pytest.fixture
def sample_post(api_session, base_url):
    """Creates a post and returns it for use in tests."""
    new_post = {
        "title": "Fixture Post",
        "body": "Created by a pytest fixture",
        "userId": 1
    }
    response = api_session.post(f"{base_url}/posts", json=new_post)
    assert response.status_code == 201
    return response.json()

