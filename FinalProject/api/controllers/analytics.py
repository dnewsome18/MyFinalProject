from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import analytics as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    """
    Create a new analytics record.
    """
    new_entry = model.Analytics(
        metric_name=request.metric_name,
        value=request.value,
        timestamp=request.timestamp
    )

    try:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_entry


def read_all(db: Session):
    """
    Retrieve all analytics records.
    """
    try:
        result = db.query(model.Analytics).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, metric_id: int):
    """
    Retrieve a specific analytics record by ID.
    """
    try:
        record = db.query(model.Analytics).filter(model.Analytics.id == metric_id).first()
        if not record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return record


def update(db: Session, metric_id: int, request):
    """
    Update an existing analytics record by ID.
    """
    try:
        record = db.query(model.Analytics).filter(model.Analytics.id == metric_id)
        if not record.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric ID not found!")
        update_data = request.dict(exclude_unset=True)
        record.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return record.first()


def delete(db: Session, metric_id: int):
    """
    Delete an analytics record by ID.
    """
    try:
        record = db.query(model.Analytics).filter(model.Analytics.id == metric_id)
        if not record.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric ID not found!")
        record.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
