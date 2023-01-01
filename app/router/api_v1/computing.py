from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import Computing 

router = APIRouter(
    prefix="/Computing",
    tags=["Computing"],
    # dependencies=[Depends(get_token_header)],
)