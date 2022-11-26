from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas import User, Item
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.models import User, Item
from app.database import Sessionlocal, engine

from app import settings

import os
from dotenv import load_dotenv
load_dotenv('.env.local')

app = FastAPI(
   title=settings.project_name,
   version=settings.version,
   openapi_url=f"{settings.api_v1_prefix}/openapi.json",
   debug=settings.debug
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

 #to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/Items")
def read_root(token: str = Depends(oauth2_scheme)):
    return {"Hello": "World"}