from security import get_password_hash

users = {
    "admin@example.com": {
        "email": "admin@example.com",
        "password": get_password_hash("admin123")
    }
}