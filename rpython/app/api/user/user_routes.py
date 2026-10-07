from fastapi import APIRouter, HTTPException, status

from .user_models import User
from .user_api import (
    get_all_users,  
    get_user,
    create_user,    
    update_user,
    delete_user 
)



router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
def get_users_endpoint():
    """Get all users."""
    return get_all_users()      

@router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user_endpoint(user_id: int):
    """Get a user by ID."""
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/create", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: User):
    """Create a new user."""
    return create_user(user)    

@router.put("/update/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def update_user_endpoint(user_id: int, updated_user: User):
    """Update a user by ID."""
    user = update_user(user_id, updated_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int):
    """Delete a user by ID."""
    user = delete_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return None