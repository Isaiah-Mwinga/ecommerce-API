from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import categories
from app import models,crud

router = APIRouter(
    prefix="/Categories",
    tags=["Categories"],
    # dependencies=[Depends(get_token_header)],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
