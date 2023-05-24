from . import models, schemas
from sqlalchemy.orm import Session


def create_user_in_db(user: schemas.User, db: Session) -> models.User:
    new_user = models.User(name=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(email: str, db: Session) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(user_id: int, db: Session) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_all_users(db: Session) -> list[models.User]:
    return db.query(models.User).all()


def delete_user_in_db(user_id: int, db: Session):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()