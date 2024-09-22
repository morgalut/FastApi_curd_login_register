"""
This module handles JWT creation and decoding for authentication purposes.
It uses the HS256 algorithm and provides utility functions to create and decode JWT tokens.
"""

from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException

# Secret key to encode the JWT (Should be changed to a secure, random key in production)
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a JWT token with the given data and expiration time.

    Args:
        data (dict): The data to include in the token.
        expires_delta (timedelta, optional): The expiration time for the token. 
                                             Defaults to ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """
    Decodes a JWT token and retrieves the user information.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The payload decoded from the token if valid.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Could not validate credentials") from exc
