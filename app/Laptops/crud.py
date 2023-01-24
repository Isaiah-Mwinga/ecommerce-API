from fastapi import HTTPException, status
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.database import get_db
from app.Computing import models, schemas


def create_Laptops(Laptops: schemas.Laptops, db: Session) -> models.Laptops:
    db_Laptop = models.Laptops(**Laptops.dict())
    db.add(db_Laptop)
    db.commit()
    db.refresh(db_Laptop)
    return db_Laptop


def get_all_Laptops(db: Session) -> list[models.Laptops]:
    return db.query(models.Laptops).all()

def get_Laptops_by_name(name: str, db: Session) -> models.Laptops:
        return db.query(models.Laptops).filter(models.Laptops.name == name).first()

def get_Laptops_by_id(Laptops_id: int, db: Session) -> models.Laptops:
    return db.query(models.Laptops).filter(models.Laptops.id == Laptops_id).first()

def delete_Laptops(db: Session, Laptops_id: int):
    db.query(models.Laptops).filter(models.Laptops.id == id).delete()
    db.commit()
    
