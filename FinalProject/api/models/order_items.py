from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .orders import Order
from ..dependencies.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    item_id = Column(Integer, ForeignKey("menu_items.item_id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="order_items")
    item = relationship("MenuItem", back_populates="order_items")