from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import permissions as controller
from ..schemas import permissions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Permissions"],
    prefix="/permissions"
)

@router.post("/", response_model=schema.Permission)
def create(request: schema.PermissionCreate, db: Session = Depends(get_db)):
   return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Permission])
def read_all(db: Session = Depends(get_db)):
   return controller.read_all(db)


@router.get("/{permission_id}", response_model=schema.Permission)
def read_one(permission_id: int, db: Session = Depends(get_db)):
   return controller.read_one(db, permission_id=permission_id)


@router.put("/{permission_id}", response_model=schema.Permission)
def update(permission_id: int, request: schema.PermissionUpdate, db: Session = Depends(get_db)):
   return controller.update(db=db, request=request, permission_id=permission_id)


@router.delete("/{permission_id}")
def delete(permission_id: int, db: Session = Depends(get_db)):
   return controller.delete(db=db, permission_id=permission_id)