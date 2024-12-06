from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Sandwich(BaseModel):
    id: int
    name: str
    ingredients: str
    description: str

class SandwichBase(BaseModel):
    sandwich_name: str
    price: float

class SandwichCreate(BaseModel):
    name: str
    ingredients: str
    description: str

class SandwichUpdate(BaseModel):
    name: Optional[str] = None
    ingredients: Optional[str] = None
    description: Optional[str] = None


class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True