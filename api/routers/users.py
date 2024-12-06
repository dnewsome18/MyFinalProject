from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import users as controller
from ..schemas import users as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Users"],
    prefix="/users"
)

@router.post("/users/", response_model=schema.User, tags=["Users"])
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=user)

@router.get("/users/", response_model=list[schema.User], tags=["Users"])
def read_users(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/users/{user_id}", response_model=schema.User, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = controller.read_one(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=schema.User, tags=["Users"])
def update_user(user_id: int, user: schema.UserUpdate, db: Session = Depends(get_db)):
    db_user = controller.read_one(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return controller.update(db=db, request=user, user_id=user_id)

@router.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = controller.read_one(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return controller.delete(db=db, user_id=user_id)