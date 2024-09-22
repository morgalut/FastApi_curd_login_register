# C:\Users\Mor\Desktop\fastapi_py\fastapi_project\app\schemas\task_schema.py
 
from pydantic import BaseModel
from typing import Optional
from app.enums import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: TaskPriority

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority

    class Config:
        orm_mode = True
