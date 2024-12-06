from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import order_items as controller
from ..schemas import order_items as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Order Items"],
    prefix="/order-items"
)

@router.post("/order-items/", response_model=schema.OrderItem, tags=["Order Items"])
def create_order_item(item: schema.OrderItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=item)

@router.get("/order-items/", response_model=list[schema.OrderItem], tags=["Order Items"])
def read_order_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/order-items/{order_item_id}", response_model=schema.OrderItem, tags=["Order Items"])
def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    item = controller.read_one(db, order_item_id=order_item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return item

@router.put("/order-items/{order_item_id}", response_model=schema.OrderItem, tags=["Order Items"])
def update_order_item(order_item_id: int, item: schema.OrderItemUpdate, db: Session = Depends(get_db)):
    db_item = controller.read_one(db, order_item_id=order_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return controller.update(db=db, order_item_id=order_item_id, request=item)

@router.delete("/order-items/{order_item_id}", tags=["Order Items"])
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    db_item = controller.read_one(db, order_item_id=order_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return controller.delete(db=db, order_item_id=order_item_id)