from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Promotions"],
    prefix="/promotions"
)


@router.post("", response_model=schema.Promotion, tags=["Promotions"])
def create_promotion(promotion: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=promotion)

@router.get("/", response_model=list[schema.Promotion], tags=["Promotions"])
def read_promotions(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promo_id}", response_model=schema.Promotion, tags=["Promotions"])
def read_promotion(promo_id: int, db: Session = Depends(get_db)):
    promotion = controller.read_one(db, promo_id=promo_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion

@router.put("/{promo_id}", response_model=schema.Promotion, tags=["Promotions"])
def update_promotion(promo_id: int, promotion: schema.PromotionUpdate, db: Session = Depends(get_db)):
    db_promotion = controller.read_one(db, promo_id=promo_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return controller.update(db=db, promo_id=promo_id, request=promotion)

@router.delete("/{promo_id}", response_model=dict, tags=["Promotions"])
def delete_promotion(promo_id: int, db: Session = Depends(get_db)):
    db_promotion = controller.read_one(db, promo_id=promo_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    controller.delete(db=db, promo_id=promo_id)
    return {"message": "Promotion deleted successfully"}
