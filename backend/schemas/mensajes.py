from pydantic import BaseModel
from datetime import datetime


class MensajeLogCreate(BaseModel):
    mensaje: str
    status: str | None = "sent"
    
    
class MensajeLogUpdate(BaseModel):
    mensaje: str | None = None
    status: str | None = None
    
    
class MensajeLogRead(BaseModel):
    id: str
    mensaje: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


# =========== Adecuaciones del response para enciar en whats ==============
class MensajeLogListResponse(BaseModel):
    status: str
    data: list[MensajeLogRead]
    whats_response: str | None = None


class MensajeLogItemResponse(BaseModel):
    status: str
    data: MensajeLogRead
    whats_response: str | None = None


class MensajeDeleteResponse(BaseModel):
    status: str
    data: dict
    whats_response: str | None = None
