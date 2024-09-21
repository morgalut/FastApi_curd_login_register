from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.services.task_service import TaskService
from app.database import SessionLocal
from app.enums import TaskStatus

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.create_task(task)

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.get_tasks()

@router.patch("/tasks/{task_id}/status")
def update_task_status(task_id: int, status: TaskStatus, db: Session = Depends(get_db)):
    service = TaskService(db)
    task = service.update_task_status(task_id, status)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
