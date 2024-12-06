from sqlalchemy import Column, Integer, String, Text, DECIMAL, Date
from ..dependencies.database import Base
from sqlalchemy.ext.declarative import declarative_base


class Promotion(Base):
    __tablename__ = "promotions"

    promo_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(20), nullable=False)
    description = Column(Text, nullable=True)
    discount_percent = Column(DECIMAL(5, 2), nullable=False)
    valid_until = Column(Date, nullable=False)
