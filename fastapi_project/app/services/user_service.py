"""
This module provides services related to user management,
including creating users, retrieving users by username, and verifying passwords.
"""

from passlib.context import CryptContext  # Third-party import
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    """
    UserService provides methods for managing users in the database,
    such as creating users, querying users, and password verification.
    """

    def __init__(self, db: Session):
        """
        Initialize UserService with a database session.

        Args:
            db (Session): The database session to be used for database operations.
        """
        self.db = db

    def get_user_by_username(self, username: str):
        """
        Retrieve a user by their username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: The user object if found, or None if no user exists with that username.
        """
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, user: UserCreate):
        """
        Create a new user in the database.

        Args:
            user (UserCreate): The user data including username, email, and password.

        Returns:
            User: The newly created user object.
        """
        hashed_password = pwd_context.hash(user.password)
        db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def verify_password(self, plain_password: str, hashed_password: str):
        """
        Verify if the provided plain password matches the hashed password.

        Args:
            plain_password (str): The plain text password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return pwd_context.verify(plain_password, hashed_password)
