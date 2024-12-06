import logging
from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from ..models.orders import Order

class OrderRequest(BaseModel):
    customer_name: str
    description: str

def create(db: Session, request: OrderRequest):
    try:
        new_item = Order(
            customer_name=request.customer_name,
            description=request.description
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        print(f"SQLAlchemy Error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create order: {str(e)}"
        )
    return new_item


def read_all(db: Session):
    try:
        return db.query(Order).all()
    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemyError: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve orders."
        )


def read_one(db: Session, item_id: int):
    try:
        item = db.query(Order).filter(Order.id == item_id).first()
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found."
            )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve the order."
        )
    return item


def update(db: Session, item_id: int, request: OrderRequest):
    try:
        item = db.query(Order).filter(Order.id == item_id)
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found."
            )
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update order."
        )
    return item.first()


def delete(db: Session, item_id: int):
    try:
        item = db.query(Order).filter(Order.id == item_id)
        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found."
            )
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete order."
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
