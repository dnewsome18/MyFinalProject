from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
