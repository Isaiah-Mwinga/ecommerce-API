from app.computing import models, schemas
from app.database import get_db

def create_computing(db: Session, computing: schemas.Computing):
    db_computing = models.Computing(name=computing.name)
    db.add(db_computing)
    db.commit()
    db.refresh(db_computing)
    return db_computing


def get_computing_by_id(db: Session, computing_id: int) -> models.Computing:
     return db.query(models.Computing).filter(models.Computing.id == computing_id).first()

def get_all_computing(db: Session) -> list[models.Computing]:
         return db.query(models.Computing).all()

def delete_computing(db: Session, computing_id: int):
    db.query(models.Computing).filter(models.Computing.id == computing_id).delete()
    db.commit()

