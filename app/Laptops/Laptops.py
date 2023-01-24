from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.Laptops import  crud
from app.Computing import moels, schemas

router = APIRouter(tags=["Laptops"], prefix="/Laptops")

@router.post("/Laptops/",status_code=status.HTTP_201_CREATED, response_model=schemas.Laptops)
def create_Laptops(Laptops: schemas.Laptops, db: Session = Depends(get_db)):
    if crud.get_Laptops_by_name(Laptops.name, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Laptops already exists")
    return crud.create_Laptops(Laptops, db)