from sqlalchemy.orm import Session
from app.Categories import models, schemas

def create_category(category: schemas.Category, db: Session) -> models.Category:
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_all_categories(db: Session) -> list[models.Category]:
        return dbquery(models.Category).all()

def get_category_by_name(name: str, db: Session) -> models.Category:
        return db.query(models.Category).filter(models.Category.name == name).first()


def get_category_by_id(category_id: int, db: Session) -> models.Category:
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def delete_category(category_id: int, db: Session):
    db.query(models.Category).filter(models.Category.id == category_id).delete()
    db.commit()


