from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.user_service import UserService
from app.database import SessionLocal
from app.security import create_access_token  # This import should work now

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    if service.get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return service.create_user(user)

@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    service = UserService(db)
    db_user = service.get_user_by_username(user.username)
    if not db_user or not service.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.username})  # Create token for the user
    return {"token": token, "message": "Login successful"}
