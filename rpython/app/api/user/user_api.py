from pathlib import Path
from .user_models import User
from .user_ops import (
    read_users,
    write_users
)

def get_all_users():
    """Get all users."""
    return read_users()

def get_user(user_id: int):
    """Get a user by ID."""
    users = read_users()
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def create_user(user: User):
    """Create a new user and save it to the JSON file."""
    users = read_users()
    new_id = max([u["id"] for u in users], default=0) + 1
    user_dict = user.dict()
    user_dict["id"] = new_id
    users.append(user_dict)
    write_users(users)
    return user_dict    

def update_user(user_id: int, updated_user: User):
    """Update a user by ID."""
    users = read_users()
    for i, user in enumerate(users):
        if user["id"] == user_id:
            updated_user_dict = updated_user.dict()
            updated_user_dict["id"] = user_id
            users[i] = updated_user_dict
            write_users(users)
            return updated_user_dict
    return None

def delete_user(user_id: int):
    """Delete a user by ID."""
    users = read_users()
    users = [user for user in users if user["id"] != user_id]
    write_users(users)