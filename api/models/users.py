from sqlalchemy import Column, Enum, Integer, String, TIMESTAMP
from datetime import datetime
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    role = Column(Enum("guest", "customer", "manager", "developer"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
