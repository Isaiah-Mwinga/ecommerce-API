from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.Computing import models, schemas
from app.database import get_db
from app.Datastorage import crud

router = APIRouter(
    prefix="/Datastorage",
    tags=["Datastorage"],
)

@router.post("/Datastorage/",status_code=status.HTTP_201_CREATED, response_model=schemas.Datastorage)
def create_Datastorage(Datastorage: schemas.Datastorage, db: Session = Depends(get_db)):
    if crud.get_Datastorage_by_name(Datastorage.name, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Datastorage already exists")
    return crud.create_Datastorage(Datastorage, db)

@router.get("/Datastorage/all", status_code=status.HTTP_200_OK, response_model=list[schemas.Datastorage])
def get_all_Datastorage(db: Session = Depends(get_db)):
    return crud.get_all_Datastorage(db)

@router.get("/Datastorage/{Datastorage_id}", status_code=status.HTTP_200_OK, response_model=schemas.Datastorage)
def get_Datastorage_by_id(Datastorage_id: int, db: Session = Depends(get_db)):
    db_Datastorage = crud.get_Datastorage_by_id(Datastorage_id, db)
    if not db_Datastorage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Datastorage not found")
    return db_Datastorage
    