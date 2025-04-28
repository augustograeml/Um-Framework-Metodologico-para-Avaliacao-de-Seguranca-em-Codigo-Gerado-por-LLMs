from fastapi import APIRouter, Depends, HTTPException
from app.auth.dependencies import get_current_user
from app.auth.jwt import create_access_token
from app.auth.password import hash_password, verify_password
from app.users.models import User
from app.users.schemas import UserCreate, UserOut
from app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user