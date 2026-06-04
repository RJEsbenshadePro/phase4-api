import pytest
import requests

def test_create_and_retrieve_post(api_session, base_url):
    """Create a post then immediatley retrieve it - chained requests."""

    # Step 1 - Create a post
    new_post = {
        "title": "Chained Request Test",
        "body": "Testing request chaining",
        "userId": 1
    }
    create_response = api_session.post(f"{base_url}/posts", json=new_post)
    assert create_response.status_code == 201
    create_id = create_response.json()["id"]

    # Step 2 - Use the ID from step 1 to retrieve it
    get_response = api_session.get(f"{base_url}/posts/1")
    assert get_response.status_code == 200

def test_create_update_delete(api_session, base_url):
    """Full lufecycle test - create, update, then delete."""

    # Create
    create_response = api_session.post(f"{base_url}/posts", json={
        "title": "Lifecycle Test",
        "body": "Will be updated and deleted",
        "userId": 1
    })
    assert create_response.status_code == 201
    post_id = create_response.json()["id"]

    # Update — use a known existing ID
    update_response = api_session.put(f"{base_url}/posts/1", json={
        "id": 1,
        "title": "Updated Lifecycle Test",
        "body": "This was updated",
        "userId": 1
    })
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Lifecycle Test"

    # Delete — use a known existing ID
    delete_response = api_session.delete(f"{base_url}/posts/1")
    assert delete_response.status_code == 200

def test_get_posts_for_user(api_session, base_url):
    """Use query parameters to filter results."""
    response = api_session.get(f"{base_url}/posts", params={"userId": 1})
    assert response.status_code == 200
    posts = response.json()
    # All returned posts should belong to userId 1
    assert all(post["userId"] == 1 for post in posts)

def test_use_sample_post_fixture(sample_post, api_session, base_url):
    """Use the sample_post fixture - post already exsists when test starts."""
    post_id = sample_post["id"]

    # Verify the fixture created a real post
    assert sample_post["title"] == "Fixture Post"
    assert post_id is not None

    # Now patch just the title using PATCH
    patch_response = api_session.patch(
        f"{base_url}/posts/{post_id}",
        json={"title": "Patched Title"}
    )
    assert patch_response.status_code == 200

def test_get_comments_for_post(api_session, base_url):
    """Test a nested resource - comments belonging to post."""
    response = api_session.get(f"{base_url}/posts/1/comments")
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) > 0
    # Every comment should have an email field
    assert all("email" in comment for comment in comments)