from sqlalchemy.orm import Session
from ..models import SystemDoc
from ..schemas import system_docs as schema

def create(db: Session, request: schema.SystemDocCreate):
    db_doc = SystemDoc(
        name=request.name,
        description=request.description,
        content=request.content
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def read_all(db: Session):
    return db.query(SystemDoc).all()

def read_one(db: Session, doc_id: int):
    return db.query(SystemDoc).filter(SystemDoc.id == doc_id).first()

def update(db: Session, request: schema.SystemDocUpdate, doc_id: int):
    db_doc = db.query(SystemDoc).filter(SystemDoc.id == doc_id).first()
    if db_doc:
        db_doc.name = request.name
        db_doc.description = request.description
        db_doc.content = request.content
        db.commit()
        db.refresh(db_doc)
    return db_doc

def delete(db: Session, doc_id: int):
    db_doc = db.query(SystemDoc).filter(SystemDoc.id == doc_id).first()
    if db_doc:
        db.delete(db_doc)
        db.commit()
    return db_doc
