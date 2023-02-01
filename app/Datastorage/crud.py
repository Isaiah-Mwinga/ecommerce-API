from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.Computing import models, schemas


def create_Datastorage(Datastorage: schemas.Datastorage, db: Session) -> models.Datastorage:
    db_Datastorage = models.Datastorage(**Datastorage.dict())
    db.add(db_Datastorage)
    db.commit()
    db.refresh(db_Datastorage)
    return db_Datastorage

def get_Datastorage_by_name(name: str, db: Session) -> models.Datastorage:
    return db.query(models.Datastorage).filter(models.Datastorage.name == name).first()

def get_Datastorage_by_id(Datastorage_id: int, db: Session) -> models.Datastorage:
    return db.query(models.Datastorage).filter(models.Datastorage.id == Datastorage_id).first()

def get_all_Datastorage(db: Session) -> list[models.Datastorage]:
    return db.query(models.Datastorage).all()
