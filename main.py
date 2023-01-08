import os   
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import SessionLocal, engine, Base


Base.metadata.create_all(engine)

from fastapi import APIRouter
from app import auth
from app.router.api_v1 import Users, Items, Categories, Computing

app = FastAPI()
app.include_router(Users.router)
app.include_router(Items.router)
app.include_router(Categories.router)
app.include_router(Computing.router)
#app.include_router(auth.router)



# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

