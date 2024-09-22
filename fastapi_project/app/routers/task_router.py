from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
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

# New: Update a task's details
@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    service = TaskService(db)
    task = service.update_task(task_id, task_update)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# New: Delete a task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    success = service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
