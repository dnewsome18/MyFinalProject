from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import system_docs as controller
from ..schemas import system_docs as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["System Docs"],
    prefix="/systemdocs"
)

@router.post("/system_docs/", response_model=schema.SystemDoc, tags=["SystemDocs"])
def create_system_doc(doc: schema.SystemDocCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=doc)

@router.get("/system_docs/", response_model=list[schema.SystemDoc], tags=["SystemDocs"])
def read_system_docs(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/system_docs/{doc_id}", response_model=schema.SystemDoc, tags=["SystemDocs"])
def read_system_doc(doc_id: int, db: Session = Depends(get_db)):
    doc = controller.read_one(db, doc_id=doc_id)
    if doc is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.put("/system_docs/{doc_id}", response_model=schema.SystemDoc, tags=["SystemDocs"])
def update_system_doc(doc_id: int, doc: schema.SystemDocUpdate, db: Session = Depends(get_db)):
    db_doc = controller.read_one(db, doc_id=doc_id)
    if db_doc is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return controller.update(db=db, doc_id=doc_id, request=doc)

@router.delete("/system_docs/{doc_id}", tags=["SystemDocs"])
def delete_system_doc(doc_id: int, db: Session = Depends(get_db)):
    db_doc = controller.read_one(db, doc_id=doc_id)
    if db_doc is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return controller.delete(db=db, doc_id=doc_id)