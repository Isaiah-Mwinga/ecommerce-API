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
async def login(form_data: OAuth2PasswordRequestForm = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_dict = db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User(**user_dict)
    hashed_password = password(form_data.password)
    if not hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
