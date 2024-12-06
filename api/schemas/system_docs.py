from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SystemDocBase(BaseModel):
    title: str
    content: str


class SystemDocCreate(SystemDocBase):
    pass


class SystemDocUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class SystemDoc(SystemDocBase):
    doc_id: int
    last_updated: datetime

    class Config:
        orm_mode = True
