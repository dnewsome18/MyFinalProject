from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import order_items as controller
from ..schemas import order_items as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Order Items"],
    prefix="/order-items"
)

@router.post("/", response_model=schema.OrderItem)
def create_order_item(request: schema.OrderItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderItem])
def read_all_order_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_item_id}", response_model=schema.OrderItem)
def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_item_id=order_item_id)

@router.put("/{order_item_id}", response_model=schema.OrderItem)
def update_order_item(order_item_id: int, request: schema.OrderItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_item_id=order_item_id)

@router.delete("/{order_item_id}")
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_item_id=order_item_id)
