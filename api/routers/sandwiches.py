from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import sandwiches as controller
from ..schemas import sandwiches as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Sandwiches"],
    prefix="/sandwiches"
)

@router.post("/sandwiches/", response_model=schema.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schema.SandwichCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=sandwich)

@router.get("/sandwiches/", response_model=list[schema.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/sandwiches/{sandwich_id}", response_model=schema.Sandwich, tags=["Sandwiches"])
def read_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = controller.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

@router.put("/sandwiches/{sandwich_id}", response_model=schema.Sandwich, tags=["Sandwiches"])
def update_sandwich(sandwich_id: int, sandwich: schema.SandwichUpdate, db: Session = Depends(get_db)):
    db_sandwich = controller.read_one(db, sandwich_id=sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return controller.update(db=db, sandwich_id=sandwich_id, request=sandwich)

@router.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = controller.read_one(db, sandwich_id=sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return controller.delete(db=db, sandwich_id=sandwich_id)