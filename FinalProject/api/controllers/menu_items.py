from sqlalchemy.orm import Session
from ..models import MenuItem
from ..schemas import menu_items as schema

def create(db: Session, request: schema.MenuItemCreate):
    db_item = MenuItem(
        title=request.title,
        description=request.description,
        price=request.price,
        category_id=request.category_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(MenuItem).all()

def read_one(db: Session, item_id: int):
    return db.query(MenuItem).filter(MenuItem.id == item_id).first()

def update(db: Session, request: schema.MenuItemUpdate, item_id: int):
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if db_item:
        db_item.title = request.title
        db_item.description = request.description
        db_item.price = request.price
        db.commit()
        db.refresh(db_item)
    return db_item

def delete(db: Session, item_id: int):
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
