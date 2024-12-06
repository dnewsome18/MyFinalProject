from pydantic import BaseModel
from typing import Optional


class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_active: bool

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None


class MenuItem(MenuItemBase):
    id: int

    class Config:
        orm_mode = True
