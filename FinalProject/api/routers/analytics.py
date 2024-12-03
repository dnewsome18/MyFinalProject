from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import analytics as controller
from ..schemas import analytics as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Analytics"],
    prefix="/analytics"
)

@router.post("/", response_model=schema.Analytic)
def create(request: schema.AnalyticCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Analytic])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{analytic_id}", response_model=schema.Analytic)
def read_one(analytic_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, analytic_id=analytic_id)

@router.put("/{analytic_id}", response_model=schema.Analytic)
def update(analytic_id: int, request: schema.AnalyticUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, analytic_id=analytic_id)

@router.delete("/{analytic_id}")
def delete(analytic_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, analytic_id=analytic_id)
