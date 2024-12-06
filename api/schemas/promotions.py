from pydantic import BaseModel
from typing import Optional
from datetime import date


class PromotionBase(BaseModel):
    code: str
    description: Optional[str] = None
    discount_percent: float
    valid_until: date

class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    description: Optional[str] = None
    discount_percent: Optional[float] = None
    valid_until: Optional[date] = None


class Promotion(PromotionBase):
    promo_id: int

    class Config:
        orm_mode = True
