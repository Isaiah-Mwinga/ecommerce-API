from sqlalchemy.orm import Session
from app.database import SessionLocal


from app.schemas import User


from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.categories).offset(skip).limit(limit).all()


def create_category(db: Session, categories: schemas.categories):
    db_category = models.categories(name=categories.name, description=categories.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
