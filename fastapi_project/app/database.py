"""
This module handles database connections and operations using SQLAlchemy.
It sets up the engine, session, and base model, and provides a function to create database tables.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables(base_class):
    """
    Create all database tables defined in the given base class.

    Args:
        base_class: The declarative base class that contains the table metadata.
    """
    base_class.metadata.create_all(bind=engine)
