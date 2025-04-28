from fastapi import FastAPI
from app.database.db import get_db_session
from app.auth.auth import UserAuth

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Initialize the database connection
    await get_db_session()

@app.post("/register")
async def register(user: dict):
    auth = UserAuth()
    return await auth.register(user)

@app.post("/login")
async def login(user: dict):
    auth = UserAuth()
    return await auth.login(user)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)