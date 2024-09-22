"""
This module defines the User model for the application, representing
users in the database with attributes such as username, email,
and hashed password.
"""

from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    """
    Represents a user in the application.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user, must be unique.
        email (str): The user's email address, must be unique.
        hashed_password (str): The hashed password of the user.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def __repr__(self):
        """Return a string representation of the User object."""
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
