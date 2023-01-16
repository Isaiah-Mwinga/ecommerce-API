from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import  OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import timedelta
from . import schemas, services
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    tags=["authentication"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login", response_model=schemas.Token)
def login(form: OAuth2PasswordRequestForm = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = services.authenticate_user(email=form.username, password=form.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}