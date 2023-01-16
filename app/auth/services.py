from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database import get_db
from app.Users.crud import get_user_by_email
from app.Users.hashing import verify_password
from app.Users   import models, schemas
from app.Users.schemas import User

SECRET_KEY = '94c9a781047fbfce8393bbe88802577e2f16402d4c8691accb0b22eba110814c'
ALGORITHM = 'HS256'
DEFAULT_EXPIRES_DELTA = 15

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def fake_hash_password(password: str):
    return "fakehashed" + password

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(db, token)
    return user     

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user  

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


#def authenticate_user(email: str, password: str, db: Session) -> models.User | bool:
#    user = get_user_by_email(email, db)
#    if not user:
#        return False
#    if not verify_password(password, user.password):
#        return False
#
#    return user
#
#
#def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
#    to_encode = data.copy()
#    if expires_delta:
#        expire = datetime.now() + expires_delta
#    else:
#        expire = datetime.now() + timedelta(minutes=DEFAULT_EXPIRES_DELTA)
#    to_encode.update({'exp': expire})
#    encoded_data = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#    return encoded_data
#
#
#def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> schemas.DisplayUser:
#    credential_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                     detail='Can not validate credentials',
#                                     headers={'WWW_Authenticate': 'Bearer'})
#    try:
#        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
#        email = payload.get('sub')
#        if email is None:
#            raise credential_error
#    except JWTError:
#        raise credential_error
#
#    user = get_user_by_email(email, db)
#
#    return schemas.DisplayUser.from_orm(user)