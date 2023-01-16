from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.Categories import schemas, crud

router = APIRouter(tags=["Categories"], prefix="/categories")


@router.post("/", response_model=schemas.Category)