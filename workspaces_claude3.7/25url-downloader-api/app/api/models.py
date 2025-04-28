from pydantic import BaseModel
from typing import Optional

class DownloadRequest(BaseModel):
    url: str

class DownloadResponse(BaseModel):
    filename: str
    message: Optional[str] = None
    error: Optional[str] = None