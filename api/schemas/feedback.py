from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FeedbackBase(BaseModel):
    user_id: Optional[int] = None
    feedback_text: str


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(BaseModel):
    feedback_text: Optional[str] = None


class Feedback(FeedbackBase):
    feedback_id: int
    created_at: datetime

    class Config:
        orm_mode = True
