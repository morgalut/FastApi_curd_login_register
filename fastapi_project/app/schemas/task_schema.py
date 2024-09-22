"""
This module defines the schemas used for task creation, updating, and responses
in the FastAPI project. It includes Pydantic models for input validation and serialization.
"""

from typing import Optional
from pydantic import BaseModel
from app.enums import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    """
    Schema for creating a new task.

    Attributes:
        title (str): The title of the task.
        description (str): A brief description of the task.
        priority (TaskPriority): The priority level of the task.
    """
    title: str
    description: str
    priority: TaskPriority

class TaskUpdate(BaseModel):
    """
    Schema for updating an existing task.

    Attributes:
        title (Optional[str]): The new title of the task (optional).
        description (Optional[str]): The new description of the task (optional).
        status (Optional[TaskStatus]): The new status of the task (optional).
        priority (Optional[TaskPriority]): The new priority level of the task (optional).
    """
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None

class TaskResponse(BaseModel):
    """
    Schema for task response after a task has been created or fetched.

    Attributes:
        id (int): The unique identifier of the task.
        title (str): The title of the task.
        description (str): The description of the task.
        status (TaskStatus): The current status of the task.
        priority (TaskPriority): The current priority level of the task.
    """
    id: int
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority

    class Config:
        """
        Configuration for Pydantic ORM mode, allowing Pydantic to work with
        SQLAlchemy models.
        """
        orm_mode = True
