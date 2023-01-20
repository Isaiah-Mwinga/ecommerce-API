from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.Categories import schemas, crud

router = APIRouter(tags=["Categories"], prefix="/categories")


@router.post("/category/",status_code=status.HTTP_201_CREATED, response_model=schemas.Category)
def create_category(category: schemas.Category, db: Session = Depends(get_db)):
    if crud.get_category_by_name(category.name, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exists")
    return crud.create_category(category, db)

@router.get("/category/all", status_code=status.HTTP_200_OK, response_model=list[schemas.Category])
def get_all_categories(db: Session = Depends(get_db)):
    return crud.get_all_categories(db)

@router.get("/category/{category_id}", status_code=status.HTTP_200_OK, response_model=schemas.Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_id(category_id, db)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return db_category    

@router.put("/category/{category_id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Category)
def update_category(category_id: int, category: schemas.Category, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_id(category_id, db)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return crud.update_category(category_id, category, db)

@router.delete("/category/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_id(category_id, db)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    crud.delete_category(category_id, db)