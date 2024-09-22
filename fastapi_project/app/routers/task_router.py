"""
This module defines the task-related API routes for task creation, retrieval,
status updates, and deletion. It uses FastAPI to define the routes and
SQLAlchemy for database operations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import TaskService
from app.database import SessionLocal
from app.enums import TaskStatus

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

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task in the database.

    Args:
        task (TaskCreate): The task details for creation.
        db (Session): The database session.

    Returns:
        TaskResponse: The created task with its details.
    """
    service = TaskService(db)
    return service.create_task(task)

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    """
    Retrieve all tasks from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[TaskResponse]: A list of all tasks.
    """
    service = TaskService(db)
    return service.get_tasks()

@router.patch("/tasks/{task_id}/status")
def update_task_status(task_id: int, status: TaskStatus, db: Session = Depends(get_db)):
    """
    Update the status of a task.

    Args:
        task_id (int): The ID of the task to update.
        status (TaskStatus): The new status for the task.
        db (Session): The database session.

    Returns:
        TaskResponse: The updated task, or raises 404 if not found.
    """
    service = TaskService(db)
    task = service.update_task_status(task_id, status)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    """
    Update the details of an existing task.

    Args:
        task_id (int): The ID of the task to update.
        task_update (TaskUpdate): The new details to update the task with.
        db (Session): The database session.

    Returns:
        TaskResponse: The updated task, or raises 404 if not found.
    """
    service = TaskService(db)
    task = service.update_task(task_id, task_update)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task from the database.

    Args:
        task_id (int): The ID of the task to delete.
        db (Session): The database session.

    Returns:
        dict: A success message, or raises 404 if the task was not found.
    """
    service = TaskService(db)
    success = service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
