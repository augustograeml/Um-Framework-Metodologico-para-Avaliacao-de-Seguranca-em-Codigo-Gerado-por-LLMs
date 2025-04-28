from fastapi import APIRouter, HTTPException
from app.downloaders.url_downloader import URLDownloader

router = APIRouter()

@router.post("/download")
async def download_url(url: str):
    downloader = URLDownloader()
    try:
        file_path = await downloader.download(url)
        return {"message": "Download successful", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))