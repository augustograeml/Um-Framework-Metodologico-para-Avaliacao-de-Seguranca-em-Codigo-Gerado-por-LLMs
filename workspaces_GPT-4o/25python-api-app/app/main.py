from fastapi import FastAPI
from app.routes.download import download_file

app = FastAPI()

@app.post("/download")
async def download(url: str):
    return await download_file(url)