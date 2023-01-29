from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.Computing import models, schemas
from app.database import get_db

def create_Desktops(Desktops: schemas.Desktops, db: Session) -> models.Desktops:
    db_Desktop = models.Desktops(**Desktops.dict())
    db.add(db_Desktop)
    db.commit()
    db.refresh(db_Desktop)
    return db_Desktop

def get_all_Desktops(db: Session) -> list[models.Desktops]:
    return db.query(models.Desktops).all()

def get_Desktops_by_name(name: str, db: Session) -> models.Desktops:
        return db.query(models.Desktops).filter(models.Desktops.name == name).first()

def get_Desktops_by_id(Desktops_id: int, db: Session) -> models.Desktops:
    return db.query(models.Desktops).filter(models.Desktops.id == Desktops_id).first()

def delete_Desktops(db: Session, Desktops_id: int):
    db.query(models.Desktops).filter(models.Desktops.id == id).delete()
    db.commit()