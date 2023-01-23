from app.Computing import models, schemas
from sqlalchemy.orm import Session
from app.database import get_db

def create_computing(db: Session, computing: schemas.Computing):
    db_computing = models.Computing(**Computing.dict())
    db.add(db_computing)
    db.commit()
    db.refresh(db_computing)
    return db_computing


def get_all_computing(db: Session) -> list[models.Computing]:
    return db.query(models.Computing).all()

def get_computing_by_name( name: str, db: Session) -> models.Computing:
    return db.query(models.Computing).filter(models.Computing.name == name).first()


def get_computing_by_id( Computing_id: int, db: Session) -> models.Computing:
    return db.query(models.Computing).filter(models.Computing.id == id).first()


def delete_computing(db: Session, Computing_id: int):
    db.query(models.Computing).filter(models.Computing.id == id).delete()
    db.commit()

