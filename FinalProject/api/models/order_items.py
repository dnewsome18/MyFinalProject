from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .orders import Order
from ..dependencies.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    order_id = Column(Integer, ForeignKey("orders.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer)

    menu_item = relationship("MenuItem", back_populates="order_items")
    order = relationship("Order", back_populates="order_items")