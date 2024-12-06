from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from pydantic import BaseModel


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    order_items = relationship("OrderItem", back_populates="menu_item")


