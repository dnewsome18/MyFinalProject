from sqlalchemy.orm import Session
from ..models import Recipe
from ..schemas import recipes as schema

def create(db: Session, request: schema.RecipeCreate):
    db_recipe = Recipe(
        sandwich_id=request.sandwich_id,
        resource_id=request.resource_id,
        amount=request.amount
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_all(db: Session):
    return db.query(Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def update(db: Session, request: schema.RecipeUpdate, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe:
        db_recipe.name = request.name
        db_recipe.instructions = request.instructions
        db_recipe.ingredients = request.ingredients
        db.commit()
        db.refresh(db_recipe)
    return db_recipe

def delete(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe
