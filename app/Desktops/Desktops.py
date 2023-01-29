from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.Desktops import  crud
from app.Computing import models, schemas

router = APIRouter(tags=["Desktops"], prefix="/Desktops")

@router.post("/Desktops/",status_code=status.HTTP_201_CREATED, response_model=schemas.Desktops)
def create_Desktops(Desktops: schemas.Desktops, db: Session = Depends(get_db)):
    if crud.get_Desktops_by_name(Desktops.name, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Desktops already exists")
    return crud.create_Desktops(Desktops, db)

@router.get("/Desktops/all", status_code=status.HTTP_200_OK, response_model=list[schemas.Desktops])
def get_all_Desktops(db: Session = Depends(get_db)):
    return crud.get_all_Desktops(db)