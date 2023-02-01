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