from fastapi import APIRouter, HTTPException
from app.services.download_service import DownloadService

router = APIRouter()
download_service = DownloadService()

@router.post("/download")
async def download_content(url: str):
    try:
        file_path = await download_service.download(url)
        return {"message": "File downloaded successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))