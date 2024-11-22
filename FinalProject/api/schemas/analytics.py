from pydantic import BaseModel
from datetime import datetime


class AnalyticBase(BaseModel):
    metric: str
    value: float


class AnalyticCreate(AnalyticBase):
    pass


class AnalyticUpdate(BaseModel):
    metric: Optional[str] = None
    value: Optional[float] = None


class Analytic(AnalyticBase):
    analytic_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
