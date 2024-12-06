from sqlalchemy.orm import Session
from ..models import SystemDoc
from ..schemas import system_docs as schema
from ..models import SystemDoc

def create(db: Session, request: schema.SystemDocCreate):
    db_doc = SystemDoc(
        title=request.title,
        content=request.content
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def read_all(db: Session):
    try:
        print("Querying SystemDoc model...")
        result = db.query(SystemDoc).all()
        print(result)
        return result
    except Exception as e:
        print(f"Error: {e}")
        raise

def read_one(db: Session, doc_id: int):
    return db.query(SystemDoc).filter(SystemDoc.doc_id == doc_id).first()

def update(db: Session, request: schema.SystemDocUpdate, doc_id: int):
    db_doc = db.query(SystemDoc).filter(SystemDoc.doc_id == doc_id).first()
    if db_doc:
        if request.title:
            db_doc.title = request.title
        if request.content:
            db_doc.content = request.content
        db.commit()
        db.refresh(db_doc)
    return db_doc

def delete(db: Session, doc_id: int):
    db_doc = db.query(SystemDoc).filter(SystemDoc.doc_id == doc_id).first()
    if db_doc:
        db.delete(db_doc)
        db.commit()
    return db_doc
