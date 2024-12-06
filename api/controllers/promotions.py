from sqlalchemy.orm import Session
from ..models import Promotion
from ..schemas import promotions as schema

def create(db: Session, request: schema.PromotionCreate):
    db_promotion = Promotion(
        code=request.code,
        description=request.description,
        discount_percent=request.discount_percent,
        valid_until=request.valid_until
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def read_all(db: Session):
    return db.query(Promotion).all()

def read_one(db: Session, promo_id: int):
    try:
        promo_id = int(promo_id)
    except ValueError:
        return None
    return db.query(Promotion).filter(Promotion.promo_id == promo_id).first()

def update(db: Session, request: schema.PromotionUpdate, promo_id: int):
    db_promotion = db.query(Promotion).filter(Promotion.promo_id == promo_id).first()
    if db_promotion:
        db_promotion.code = request.code or db_promotion.code
        db_promotion.description = request.description or db_promotion.description
        db_promotion.discount_percent = request.discount_percent or db_promotion.discount_percent
        db_promotion.valid_until = request.valid_until or db_promotion.valid_until
        db.commit()
        db.refresh(db_promotion)
    return db_promotion

def delete(db: Session, promo_id: int):
    db_promotion = db.query(Promotion).filter(Promotion.promo_id == promo_id).first()
    if db_promotion:
        db.delete(db_promotion)
        db.commit()
    return db_promotion
