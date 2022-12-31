from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import categories

router = APIRouter(
    prefix="/Categories",
    tags=["Categories"],
    # dependencies=[Depends(get_token_header)],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("Category/", response_model=categories)
def create_Category(category: categories, db: Session = Depends(get_db)):
    new_category = models.Category(
        name=category.name, 
        description=category.description)
    new_category = categories(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

@router.get("Categories", response_model=categories)
def read_Category(db: Session = Depends(get_db)):
    db_category = db.query(models.Category).all()
    return {categories.name: categories.description
            }

@router.get("Category/{category_id}", response_model=categories)
def read_Category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(categories.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category