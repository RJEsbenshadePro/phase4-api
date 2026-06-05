import pytest
import requests
import jsonschema
from jsonschema import validate
from schemas import POST_SCHEMA, COMMENT_SCHEMA, USER_SCHEMA

BASE_URL = "https://jsonplaceholder.typicode.com"

# --- Schema tests ---

def test_single_post_schema():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    # validate() throws an enception if schema doesn't match
    validate(instance=response.json(), schema=POST_SCHEMA)

def test_all_posts_match_schema():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    for post in posts:
        validate(instance=post, schema=POST_SCHEMA)

def test_comment_schema():
    response = requests.get(f"{BASE_URL}/comments/1")
    assert response.status_code == 200
    validate(instance=response.json(), schema=COMMENT_SCHEMA)

def test_user_schema():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    validate(instance=response.json(), schema=USER_SCHEMA)

# --- Parametized API tests ---

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_multiple_posts_schema(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=POST_SCHEMA)

@pytest.mark.parametrize("user_id, expected_post_count", [
    (1, 10),
    (2, 10),
    (3, 10),
])
def test_user_post_counts(user_id, expected_post_count):
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == expected_post_count
    for post in posts:
        validate(instance=post, schema=POST_SCHEMA)

# --- Deliberate schema failure example ---

def test_schema_catches_missing_field():
    """Demonstrates schema validation catching a bad response structure."""
    fake_response = {
        "id": 1,
        "title": "Missing userId and body fields"
        # userId and body are missing - should fail validation
    }
    with pytest.raises(jsonschema.ValidationError):
        validate(instance=fake_response, schema=POST_SCHEMA)