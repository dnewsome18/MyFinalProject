from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from datetime import datetime
from ..dependencies.database import Base


class SystemDoc(Base):
    __tablename__ = "system_docs"

    doc_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    last_updated = Column(TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)
