 
from pydantic import BaseModel
from app.enums import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: TaskPriority

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority

    class Config:
        orm_mode = True
