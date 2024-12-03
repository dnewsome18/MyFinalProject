from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import system_docs as controller
from ..schemas import system_docs as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["System Docs"],
    prefix="/systemdocs"
)

@router.post("/", response_model=schema.SystemDoc)
def create(request: schema.SystemDocCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.SystemDoc])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{doc_id}", response_model=schema.SystemDoc)
def read_one(doc_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, doc_id=doc_id)

@router.put("/{doc_id}", response_model=schema.SystemDoc)
def update(doc_id: int, request: schema.SystemDocUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, doc_id=doc_id)

@router.delete("/{doc_id}")
def delete(doc_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, doc_id=doc_id)
