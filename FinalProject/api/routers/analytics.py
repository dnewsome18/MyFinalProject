from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from ..controllers import analytics as controller, analytics
from ..schemas import analytics as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Analytics"],
    prefix="/analytics"
)

@router.post("/", response_model=schema.Analytic, tags=["Analytics"])
def create_analytics_entry(entry: schema.AnalyticCreate, db: Session = Depends(get_db)):
    return analytics.create(db=db, request=entry)

@router.get("/", response_model=list[schema.Analytic], tags=["Analytics"])
def read_analytics_entries(db: Session = Depends(get_db)):
    return analytics.read_all(db)

@router.get("/{metric_id}", response_model=schema.Analytic, tags=["Analytics"])
def read_analytics_entry(metric_id: int, db: Session = Depends(get_db)):
    record = analytics.read_one(db, metric_id=metric_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Metric not found")
    return record

@router.put("/{metric_id}", response_model=schema.Analytic, tags=["Analytics"])
def update_analytics_entry(metric_id: int, entry: schema.AnalyticUpdate, db: Session = Depends(get_db)):
    record = analytics.read_one(db, metric_id=metric_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Metric not found")
    return analytics.update(db=db, metric_id=metric_id, request=entry)

@router.delete("/{metric_id}", tags=["Analytics"])
def delete_analytics_entry(metric_id: int, db: Session = Depends(get_db)):
    record = analytics.read_one(db, metric_id=metric_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Metric not found")
    return analytics.delete(db=db, metric_id=metric_id)
