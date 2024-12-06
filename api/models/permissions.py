from sqlalchemy import Column, Enum, Integer, String
from ..dependencies.database import Base


class Permission(Base):
    __tablename__ = "permissions"

    permission_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role = Column(Enum("guest", "customer", "manager", "developer"), nullable=False)
    action = Column(String(50), nullable=False)
