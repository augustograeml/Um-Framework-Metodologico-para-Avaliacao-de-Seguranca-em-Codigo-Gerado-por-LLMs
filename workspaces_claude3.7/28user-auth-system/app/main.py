from fastapi import FastAPI
from app.auth.routes import auth_router
from app.users.routes import user_router
from app.config.settings import settings

app = FastAPI(title="User Authentication System")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Authentication System"}