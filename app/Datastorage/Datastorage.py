from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.Computing import models, schemas
from app.database import get_db
from app.Datastorage import crud

router = APIRouter(
    prefix="/Datastorage",
    tags=["Datastorage"],
)