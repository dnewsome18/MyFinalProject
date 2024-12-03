from sqlalchemy.orm import Session
from ..models import Permission
from ..schemas import permissions as schema

def create(db: Session, request: schema.PermissionCreate):
    db_permission = Permission(
        name=request.name,
        description=request.description
    )
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def read_all(db: Session):
    return db.query(Permission).all()

def read_one(db: Session, permission_id: int):
    return db.query(Permission).filter(Permission.id == permission_id).first()

def update(db: Session, request: schema.PermissionUpdate, permission_id: int):
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if db_permission:
        db_permission.name = request.name
        db_permission.description = request.description
        db.commit()
        db.refresh(db_permission)
    return db_permission

def delete(db: Session, permission_id: int):
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if db_permission:
        db.delete(db_permission)
        db.commit()
    return db_permission
