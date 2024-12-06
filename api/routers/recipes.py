from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Recipes"],
    prefix="/recipes"
)

@router.post("/recipes/", response_model=schema.Recipe, tags=["Recipes"])
def create_recipe(recipe: schema.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=recipe)

@router.get("/recipes/", response_model=list[schema.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/recipes/{recipe_id}", response_model=schema.Recipe, tags=["Recipes"])
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = controller.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.put("/recipes/{recipe_id}", response_model=schema.Recipe, tags=["Recipes"])
def update_recipe(recipe_id: int, recipe: schema.RecipeUpdate, db: Session = Depends(get_db)):
    db_recipe = controller.read_one(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return controller.update(db=db, recipe_id=recipe_id, request=recipe)

@router.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = controller.read_one(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return controller.delete(db=db, recipe_id=recipe_id)