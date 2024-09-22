"""
This module is the entry point for the FastAPI application.
It initializes the app, includes routers, and configures the database.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from app.routers import task_router, auth_router
from app.database import create_tables, Base

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",  # Allow your frontend origin
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Your frontend URL
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
    """
    This event is triggered when the FastAPI app starts.
    It creates the necessary database tables.
    """
    create_tables(Base)

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI OOP Task Manager!"}
