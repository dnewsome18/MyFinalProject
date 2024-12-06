from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import analytics as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_entry = model.Analytic(
        metric=request.metric,
        value=request.value,
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
    try:
        result = db.query(model.Analytic).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, metric_id: int):
    try:
        record = db.query(model.Analytic).filter(model.Analytic.analytic_id == metric_id).first()
        if not record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return record


def update(db: Session, metric_id: int, request):
    try:
        record = db.query(model.Analytic).filter(model.Analytic.analytic_id == metric_id).first()
        if not record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric ID not found!")
        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(record, key, value)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return record



def delete(db: Session, metric_id: int):
    try:
        record = db.query(model.Analytic).filter(model.Analytic.analytic_id == metric_id)
        if not record.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric ID not found!")
        record.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

