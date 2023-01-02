from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import Computing 

router = APIRouter(
    prefix="/Computing",
    tags=["Computing"],
    # dependencies=[Depends(get_token_header)],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_computing(db: Session = Depends(get_db)):
    return db.query(Computing).all()
    