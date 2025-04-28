from fastapi import FastAPI
from app.routes.download import download_file

app = FastAPI()

app.include_router(download_file)