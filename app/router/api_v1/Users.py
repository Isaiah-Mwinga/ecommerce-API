from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("User/", response_model=User)
def create_user(user: User , db: Session = Depends(get_db)):
    new_user = models.User(
        username=user.username, 
        email=user.email, 
        password=user.password, 
        is_active=user.is_active)
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("Users", response_model=User)
def read_User(token: str = Depends(oauth2_scheme) , db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(User.id == user_id).all()
    return {User.name: User.description
            }

@router.get("User/{user_id}", response_model=User)
def read_User(user_id: int , db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put(path="User/{user_id}", response_model=User)
def update_User(user_id: int, user: User , db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db_user.is_active = user.is_active
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete(path="User/{user_id}", response_model=User)
def delete_User(user_id: int , db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user

# Path: app/router/api_v1/Orders.py
# Compare this snippet from app/router/api_v1/Items.py:
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
#