"""
This module defines the Task model for the application, representing
tasks in the database with attributes such as title, description,
status, and priority.
"""

from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
from app.enums import TaskStatus, TaskPriority

class Task(Base):
    """
    Represents a task in the application.

    Attributes:
        id (int): The unique identifier for the task.
        title (str): The title of the task.
        description (str): A brief description of the task.
        status (TaskStatus): The current status of the task.
        priority (TaskPriority): The priority level of the task.
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    priority = Column(Enum(TaskPriority), default=TaskPriority.MEDIUM)

    def __repr__(self):
        """Return a string representation of the Task object."""
        return f"<Task(id={self.id}, title='{self.title}', status={self.status}, priority={self.priority})>"
