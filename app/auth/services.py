from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database import get_db
from app.Users.crud import get_user_by_email
from app.Users.hashing import verify_password
from app.Users   import models, schemas

SECRET_KEY = '94c9a781047fbfce8393bbe88802577e2f16402d4c8691accb0b22eba110814c'
ALGORITHM = 'HS256'
DEFAULT_EXPIRES_DELTA = 15

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def authenticate_user(email: str, password: str, db: Session) -> models.User | bool:
    user = get_user_by_email(email, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=DEFAULT_EXPIRES_DELTA)
    to_encode.update({'exp': expire})
    encoded_data = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> schemas.DisplayUser:
    credential_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                     detail='Can not validate credentials',
                                     headers={'WWW_Authenticate': 'Bearer'})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email = payload.get('sub')
        if email is None:
            raise credential_error
    except JWTError:
        raise credential_error

    user = get_user_by_email(email, db)

    return schemas.DisplayUser.from_orm(user)