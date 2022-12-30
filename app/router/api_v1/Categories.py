from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import categories

router = APIRouter(
    prefix="Categories",
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