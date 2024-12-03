from sqlalchemy.orm import Session
from ..models import Promotion
from ..schemas import promotions as schema

def create(db: Session, request: schema.PromotionCreate):
    db_promotion = Promotion(
        code=request.code,
        description=request.description,
        discount=request.discount,
        start_date=request.start_date,
        end_date=request.end_date
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def read_all(db: Session):
    return db.query(Promotion).all()

def read_one(db: Session, promo_id: int):
    return db.query(Promotion).filter(Promotion.id == promo_id).first()

def update(db: Session, request: schema.PromotionUpdate, promo_id: int):
    db_promotion = db.query(Promotion).filter(Promotion.id == promo_id).first()
    if db_promotion:
        db_promotion.code = request.code
        db_promotion.description = request.description
        db_promotion.discount = request.discount
        db_promotion.start_date = request.start_date
        db_promotion.end_date = request.end_date
        db.commit()
        db.refresh(db_promotion)
    return db_promotion

def delete(db: Session, promo_id: int):
    db_promotion = db.query(Promotion).filter(Promotion.id == promo_id).first()
    if db_promotion:
        db.delete(db_promotion)
        db.commit()
    return db_promotion
