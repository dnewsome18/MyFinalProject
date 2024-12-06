from ..models.order_items import OrderItem
from ..schemas.order_items import OrderItemCreate, OrderItemUpdate
from sqlalchemy.orm import Session

def create(db: Session, request: OrderItemCreate):
    db_order_item = OrderItem(
        order_id=request.order_id,
        item_id=request.item_id,
        quantity=request.quantity
    )
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

def read_all(db: Session):
    return db.query(OrderItem).all()

def read_one(db: Session, order_item_id: int):
    return db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()

def update(db: Session, request: OrderItemUpdate, order_item_id: int):
    db_order_item = db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()
    if db_order_item:
        db_order_item.order_id = request.order_id
        db_order_item.item_id = request.item_id
        db_order_item.quantity = request.quantity
        db.commit()
        db.refresh(db_order_item)
    return db_order_item

def delete(db: Session, order_item_id: int):
    db_order_item = db.query(OrderItem).filter(OrderItem.order_item_id == order_item_id).first()
    if db_order_item:
        db.delete(db_order_item)
        db.commit()
    return db_order_item