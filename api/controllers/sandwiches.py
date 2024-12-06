from sqlalchemy.orm import Session
from ..models import Sandwich
from fastapi import HTTPException, status
from ..schemas import SandwichCreate, SandwichUpdate
#from ..schemas import sandwiches as schema

def get_sandwiches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sandwich).offset(skip).limit(limit).all()

def create_sandwich(db: Session, sandwich: SandwichCreate):
    try:
        db_sandwich = Sandwich(**sandwich.dict())
        print("Creating sandwich:", db_sandwich)
        db.add(db_sandwich)
        db.commit()
        db.refresh(db_sandwich)
        return db_sandwich
    except Exception as e:
        print(f"Error creating sandwich: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create sandwich")


def read_all(db: Session):
    return db.query(Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    return db_sandwich


def update(db: Session, request: SandwichUpdate, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")

    db_sandwich.name = request.name
    db_sandwich.description = request.description
    db_sandwich.ingredients = request.ingredients
    db_sandwich.price = request.price
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich


def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not db_sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")

    db.delete(db_sandwich)
    db.commit()
    return db_sandwich
