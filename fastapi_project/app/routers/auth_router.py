"""
This module defines the authentication-related API routes, including
user registration and login functionality. It uses FastAPI for routing,
SQLAlchemy for database operations, and custom security utilities for
password hashing and token generation.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.user_service import UserService
from app.database import SessionLocal
from app.security import create_access_token  # This import should work now

router = APIRouter()

def get_db():
    """
    Dependency that provides a SQLAlchemy session for database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Registers a new user in the database.

    Args:
        user (UserCreate): The user details for registration.
        db (Session): The database session.

    Returns:
        UserResponse: The newly registered user's details.

    Raises:
        HTTPException: If the username is already registered.
    """
    service = UserService(db)
    if service.get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return service.create_user(user)

@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticates a user by verifying their credentials and returns a JWT token.

    Args:
        user (UserLogin): The user's login credentials.
        db (Session): The database session.

    Returns:
        dict: A message indicating successful login and a JWT token.

    Raises:
        HTTPException: If the credentials are invalid.
    """
    service = UserService(db)
    db_user = service.get_user_by_username(user.username)
    if not db_user or not service.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.username})  # Create token for the user
    return {"token": token, "message": "Login successful"}
