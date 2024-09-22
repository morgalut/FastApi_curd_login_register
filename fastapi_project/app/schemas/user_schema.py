"""
This module defines the Pydantic schemas for user-related operations
such as creating users, logging in, and user responses.
"""

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """
    Schema representing a user with basic details.

    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        email (EmailStr): The email address of the user.
    """
    id: int
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    """
    Schema for creating a new user.

    Attributes:
        username (str): The desired username for the new user.
        email (EmailStr): The email address for the new user.
        password (str): The password for the new user.
    """
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    """
    Schema for user login.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
    """
    username: str
    password: str

class UserResponse(BaseModel):
    """
    Schema for returning user details in responses.

    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        email (EmailStr): The email address of the user.
    """
    id: int
    username: str
    email: EmailStr

    class Config:
        """
        Pydantic configuration to enable ORM mode, which allows
        returning data directly from SQLAlchemy models.
        """
        orm_mode = True
