from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas import order_details as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)

@router.post("/order-details/", response_model=schema.OrderDetail, tags=["Order Details"])
def create_order_detail(detail: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=detail)

@router.get("/order-details/", response_model=list[schema.OrderDetail], tags=["Order Details"])
def read_order_details(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/order-details/{item_id}", response_model=schema.OrderDetail, tags=["Order Details"])
def read_order_detail(item_id: int, db: Session = Depends(get_db)):
    detail = controller.read_one(db, item_id=item_id)
    if detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return detail

@router.put("/order-details/{item_id}", response_model=schema.OrderDetail, tags=["Order Details"])
def update_order_detail(item_id: int, detail: schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    db_detail = controller.read_one(db, item_id=item_id)
    if db_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return controller.update(db=db, item_id=item_id, request=detail)

@router.delete("/order-details/{item_id}", tags=["Order Details"])
def delete_order_detail(item_id: int, db: Session = Depends(get_db)):
    db_detail = controller.read_one(db, item_id=item_id)
    if db_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return controller.delete(db=db, item_id=item_id)