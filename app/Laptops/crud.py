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

    def get_Laptops_by_name(name: str, db: Session) -> models.Laptops:
        return db.query(models.Laptops).filter(models.Laptops.name == name).first()
        