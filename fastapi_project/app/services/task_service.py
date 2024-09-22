# C:\Users\Mor\Desktop\fastapi_py\fastapi_project\app\services\task_service.py

from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate  # Import TaskUpdate
from app.enums import TaskStatus

class TaskService:

    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: TaskCreate):
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
        return self.db.query(Task).all()

    def update_task_status(self, task_id: int, status: TaskStatus):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            task.status = status
            self.db.commit()
            self.db.refresh(task)
            return task
        return None

    def update_task(self, task_id: int, task_update: TaskUpdate):  # Use TaskUpdate here
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            for key, value in task_update.dict(exclude_unset=True).items():
                setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)
        return task

    # New: Delete a task
    def delete_task(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()
            return True
        return False
