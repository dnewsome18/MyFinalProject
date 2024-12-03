from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Promotions"],
    prefix="/promotions"
)

@router.post("/", response_model=schema.Promotion)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promo_id}", response_model=schema.Promotion)
def read_one(promo_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, promo_id=promo_id)

@router.put("/{promo_id}", response_model=schema.Promotion)
def update(promo_id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, promo_id=promo_id)

@router.delete("/{promo_id}")
def delete(promo_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, promo_id=promo_id)
