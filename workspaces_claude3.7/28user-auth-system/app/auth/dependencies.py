from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.users.models import User
from app.auth.jwt import verify_jwt_token

def get_current_user(token: str, db: Session = Depends(get_db)) -> User:
    user_id = verify_jwt_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user