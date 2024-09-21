from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate
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
