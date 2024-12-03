from sqlalchemy.orm import Session
from ..models import Sandwich
from ..schemas import sandwiches as schema

def create(db: Session, request: schema.SandwichCreate):
    db_sandwich = Sandwich(
        name=request.name,
        description=request.description,
        ingredients=request.ingredients,
        price=request.price
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

def update(db: Session, request: schema.SandwichUpdate, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db_sandwich.name = request.name
        db_sandwich.description = request.description
        db_sandwich.ingredients = request.ingredients
        db_sandwich.price = request.price
        db.commit()
        db.refresh(db_sandwich)
    return db_sandwich

def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
    return db_sandwich
