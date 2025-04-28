from fastapi import APIRouter, HTTPException
from app.utils.validators import validate_url
from app.services.downloader import Downloader

router = APIRouter()

@router.post("/download")
async def download_file(url: str):
    if not validate_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL")
    
    downloader = Downloader()
    try:
        content = await downloader.download(url)
        file_path = downloader.save_file(content)
        return {"message": "File downloaded successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))