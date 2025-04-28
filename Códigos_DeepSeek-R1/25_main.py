from fastapi import FastAPI
from app.routes.download_routes import router as download_router

app = FastAPI()

app.include_router(download_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the URL Downloader API"}