from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from ..dependencies.database import Base



class Analytic(Base):
    __tablename__ = "analytics"

    analytic_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    metric = Column(String(50), nullable=False)
    value = Column(DECIMAL(10, 2), nullable=False)
    timestamp = Column(DateTime, default=func.now(), nullable=False)