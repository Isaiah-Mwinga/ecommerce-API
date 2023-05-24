from fastapi import APIRouter, status, Depends, HTTPException
from app.Users.schemas import User, UserInDB
from sqlalchemy.orm import Session
from app.database import get_db
from . import crud
from app.auth.services import get_current_user
router = APIRouter(tags=['Users'], prefix='/users')


@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=UserInDB)
def create_user(user: User, db: Session = Depends(get_db)):
    if crud.get_user_by_email(user.email, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This email is already registered!')

    response = crud.create_user_in_db(user, db)
    return response


@router.get('/all', status_code=status.HTTP_200_OK, response_model=list[UserInDB])
def get_all_users(db: Session = Depends(get_db)):
    response = crud.get_all_users(db)
    return response


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=UserInDB)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {user_id} does not exist!')

    return user


#@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
#def delete_user(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#    return crud.delete_user_in_db(user_id, db)

@router.put('/user/{user_id}', status_code=status.HTTP_202_ACCEPTED, response_model=UserInDB)
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {user_id} does not exist!')

    return crud.update_user_in_db(user_id, user, db)