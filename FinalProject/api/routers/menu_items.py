from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_items as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Menu Items"],
    prefix="/menuitems"
)

@router.post("/menu-items/", response_model=schema.MenuItem, tags=["Menu Items"])
def create_menu_item(item: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=item)

@router.get("/menu-items/", response_model=list[schema.MenuItem], tags=["Menu Items"])
def read_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/menu-items/{item_id}", response_model=schema.MenuItem, tags=["Menu Items"])
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = controller.read_one(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

@router.put("/menu-items/{item_id}", response_model=schema.MenuItem, tags=["Menu Items"])
def update_menu_item(item_id: int, item: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    db_item = controller.read_one(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return controller.update(db=db, request=item, item_id=item_id)

@router.delete("/menu-items/{item_id}", tags=["Menu Items"])
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = controller.read_one(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return controller.delete(db=db, item_id=item_id)