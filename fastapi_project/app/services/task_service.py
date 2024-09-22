"""
This module provides services for managing tasks, including creating, retrieving,
updating, and deleting tasks in the database.
"""

from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.enums import TaskStatus

class TaskService:
    """
    TaskService provides methods for managing tasks in the database, 
    such as creating tasks, retrieving all tasks, updating task statuses, 
    and deleting tasks.
    """

    def __init__(self, db: Session):
        """
        Initialize TaskService with a database session.

        Args:
            db (Session): The database session to be used for database operations.
        """
        self.db = db

    def create_task(self, task: TaskCreate):
        """
        Create a new task in the database.

        Args:
            task (TaskCreate): The task data including title, description, and priority.

        Returns:
            Task: The newly created task object.
        """
        db_task = Task(
            title=task.title,
            description=task.description,
            priority=task.priority
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_tasks(self):
        """
        Retrieve all tasks from the database.

        Returns:
            List[Task]: A list of all task objects in the database.
        """
        return self.db.query(Task).all()

    def update_task_status(self, task_id: int, status: TaskStatus):
        """
        Update the status of a task.

        Args:
            task_id (int): The ID of the task to update.
            status (TaskStatus): The new status for the task.

        Returns:
            Task: The updated task object if found, or None if not found.
        """
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            task.status = status
            self.db.commit()
            self.db.refresh(task)
            return task
        return None

    def update_task(self, task_id: int, task_update: TaskUpdate):
        """
        Update a task with new information.

        Args:
            task_id (int): The ID of the task to update.
            task_update (TaskUpdate): The updated task data.

        Returns:
            Task: The updated task object if found, or None if not found.
        """
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            for key, value in task_update.dict(exclude_unset=True).items():
                setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)
        return task

    def delete_task(self, task_id: int):
        """
        Delete a task from the database.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            bool: True if the task was successfully deleted, False otherwise.
        """
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()
            return True
        return False
