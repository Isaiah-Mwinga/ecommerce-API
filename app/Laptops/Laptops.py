from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.Laptops import  crud
from app.Computing import models, schemas

router = APIRouter(tags=["Laptops"], prefix="/Laptops")

@router.post("/Laptops/",status_code=status.HTTP_201_CREATED, response_model=schemas.Laptops)
def create_Laptops(Laptops: schemas.Laptops, db: Session = Depends(get_db)):
    if crud.get_Laptops_by_name(Laptops.name, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Laptops already exists")
    return crud.create_Laptops(Laptops, db)

@router.get("/Laptops/all", status_code=status.HTTP_200_OK, response_model=list[schemas.Laptops])
def get_all_Laptops(db: Session = Depends(get_db)):
    return crud.get_all_Laptops(db)

@router.get("/Laptops/{Laptops_id}", status_code=status.HTTP_200_OK, response_model=schemas.Laptops)
def get_Laptops_by_id(Laptops_id: int, db: Session = Depends(get_db)):
    db_Laptops = crud.get_Laptops_by_id(Laptops_id, db)
    if not db_Laptops:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptops not found")
    return db_Laptops

@router.put("/Laptops/{Laptops_id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Laptops)
def update_Laptops(Laptops_id: int, Laptops: schemas.Laptops, db: Session = Depends(get_db)):
    db_Laptops = crud.get_Laptops_by_id(Laptops_id, db)
    if not db_Laptops:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptops not found")
    return crud.update_Laptops(Laptops_id, Laptops, db)

@router.delete("/Laptops/{Laptops_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Laptops(Laptops_id: int, db: Session = Depends(get_db)):
    db_Laptops = crud.get_Laptops_by_id(Laptops_id, db)
    if not db_Laptops:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptops not found")
    crud.delete_Laptops(Laptops_id, db)