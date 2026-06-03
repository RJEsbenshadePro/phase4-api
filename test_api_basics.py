import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")

    # Status code assertion
    assert response.status_code == 200

    # Parse JSON response
    posts = response.json()

    # Content assertions
    assert isinstance(posts, list)
    assert len(posts) == 100

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    post = response.json()

    # Verify the structure of a post object
    assert "id" in post
    assert "title" in post
    assert "body" in post
    assert "userId" in post

    # Verify the correct post was returned
    assert post["id"] == 1

def test_create_post():
    new_post = {
        "title": "RJ's Test Post",
        "body": "This post was created by automated API testing",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    # 201 Created is the correct status for a successful POST
    assert response.status_code == 201

    created_post = response.json()

    # Verify the response echoes back what we sent
    assert created_post["title"] == new_post["title"]
    assert created_post["body"] == new_post["body"]
    assert "id" in created_post


def test_updated_post():
    updated_data = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body content",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=updated_data)

    assert response.status_code == 200

    updated_post = response.json()
    assert updated_post["title"] == "Updated Title"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    # 200 OK is what JSONPlaceholder return for DELETE
    assert response.status_code == 200

def test_get_nonexsistent_post():
    reponse = requests.delete(f"{BASE_URL}/posts/99999")

    # This is a negitive test - we expect a 404
    assert reponse.status_code == 404

def test_response_headers():
    response = requests.get(f"{BASE_URL}/posts/1")

    # Verify content type in JSON
    assert "application/json" in response.headers["Content-Type"]

def test_response_time():
    response = requests.get(f"{BASE_URL}/posts")

    # Response should come back in under 3 seconds
    assert response.elapsed.total_seconds() < 3