from pydantic import BaseModel, HttpUrl

class WebhookRequest(BaseModel):
    url: HttpUrl
    method: str = "GET"
    headers: dict = {}
    payload: dict = {}