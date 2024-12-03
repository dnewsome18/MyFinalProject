from pydantic import BaseModel
from typing import Optional

class OrderItemBase(BaseModel):
    order_id: int
    item_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(OrderItemBase):
    order_id: Optional[int] = None
    item_id: Optional[int] = None
    quantity: Optional[int] = None

class OrderItem(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True