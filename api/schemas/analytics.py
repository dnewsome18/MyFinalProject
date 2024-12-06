from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from datetime import datetime


class Analytic(BaseModel):
    metric: str
    value: Decimal

class AnalyticCreate(BaseModel):
    metric: str
    value: float

class AnalyticUpdate(BaseModel):
    metric: Optional[str] = None
    value: Optional[float] = None

class AnalyticBase(BaseModel):
    analytic_id: int
    timestamp: datetime

    class AnalyticResponse(BaseModel):
        id: int
        name: str
        value: float

    class Config:
        orm_mode = True