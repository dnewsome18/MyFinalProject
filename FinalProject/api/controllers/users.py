from sqlalchemy.orm import Session
from ..models import User
from ..schemas import users as schema

def create(db: Session, request: schema.UserCreate):
    db_user = User(
        username=request.username,
        email=request.email,
        password=request.password,
        is_active=request.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def read_all(db: Session):
    return db.query(User).all()

def read_one(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def update(db: Session, request: schema.UserUpdate, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db_user.username = request.username if request.username else db_user.username
        db_user.email = request.email if request.email else db_user.email
        db_user.password = request.password if request.password else db_user.password
        db_user.role = request.role if request.role else db_user.role
        db.commit()
        db.refresh(db_user)
    return db_user

def delete(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
