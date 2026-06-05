import pytest
import requests
import json
from jsonschema import validate
from schemas import POST_SCHEMA, USER_SCHEMA

BASE_URL = "https://jsonplaceholder.typicode.com"

with open("test_data.json", "r") as f:
    data = json.load(f)


@pytest.mark.parametrize("post_id", data["valid_post_ids"])
def test_valid_post_ids_return_200(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=POST_SCHEMA)

@pytest.mark.parametrize("user_id", data["valid_user_ids"])
def test_valid_user_ids_return_200(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=USER_SCHEMA)

@pytest.mark.parametrize("invalid_id", data["invalid_ids"])
def test_invalid_ids_return_404(invalid_id):
    response = requests.get(f"{BASE_URL}/posts/{invalid_id}")
    assert response.status_code == 404

@pytest.mark.parametrize("post", data["new_posts"])
def test_create_posts_from_data(post):
    response = requests.post(f"{BASE_URL}/posts", json=post)
    assert response.status_code == 201
    created = response.json()
    assert created["title"] == post["title"]
    assert created["userId"] == post["userId"]
    assert "id" in created

@pytest.mark.parametrize("user_id", data["valid_user_ids"])
def test_user_posts_match_schema(user_id):
    response = requests.get(
        f"{BASE_URL}/posts",
        params={"userId": user_id}
    )
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0
    for post in posts:
        validate(instance=post, schema=POST_SCHEMA)