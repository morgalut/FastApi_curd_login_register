# C:\Users\Mor\Desktop\fastapi_py\fastapi_project\app\main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from app.routers import task_router, auth_router
from app.database import create_tables, Base
from app.models.task import Task
from app.models.user import User

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",  # Allow your frontend origin
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(task_router.router)
app.include_router(auth_router.router, prefix="/auth")

# Initialize DB
@app.on_event("startup")
async def startup_event():
    # Create tables when the app starts
    create_tables(Base)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI OOP Task Manager!"}
