from pydantic import BaseModel


class OrderItemBase(BaseModel):
    order_id: int
    item_id: int
    quantity: int
    subtotal: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    subtotal: Optional[float] = None


class OrderItem(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True
