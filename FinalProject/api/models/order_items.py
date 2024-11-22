from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .orders import Order
from ..dependencies.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_name = Column(String(255))

    order = relationship("Order", back_populates="order_items")