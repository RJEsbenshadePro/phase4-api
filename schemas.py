# --- Define schemas ---

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "userId", "title", "body"],
    "properties": {
        "id":     {"type": "integer"},
        "userId": {"type": "integer"},
        "title":  {"type": "string"},
        "body":   {"type": "string"}
    }
}

COMMENT_SCHEMA = {
    "type": "object",
    "required": ["id", "postId", "name", "email", "body"],
    "properties": {
        "id":     {"type": "integer"},
        "postId": {"type": "integer"},
        "name":   {"type": "string"},
        "email":  {"type": "string"},
        "body":   {"type": "string"}
    }
}

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email"],
    "properties": {
        "id":       {"type": "integer"},
        "name":     {"type": "string"},
        "username": {"type": "string"},
        "email":    {"type": "string"}
    }
}