from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import categories

router = APIRouter(
    prefix="Categories",
    tags=["Categories"],
    # dependencies=[Depends(get_token_header)],
)