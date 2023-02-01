from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.Computing import models, schemas


def create_Datastorage(Datastorage: schemas.Datastorage, db: Session) -> models.Datastorage:
    db_Datastorage = models.Datastorage(**Datastorage.dict())
    db.add(db_Datastorage)
    db.commit()
    db.refresh(db_Datastorage)
    return db_Datastorage
    