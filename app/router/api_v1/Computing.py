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

@router.get("/{computing_id}")
def read_computing(computing_id: int, db: Session = Depends(get_db)):
    db_computing = db.query(Computing).filter(Computing.id == computing_id).first()
    if db_computing is None:
        raise HTTPException(status_code=404, detail="Computing not found")
    return db_computing

@router.post("/")
def create_computing(computing: Computing, db: Session = Depends(get_db)):
    db_computing = Computing(**computing.dict())
    db.add(db_computing)
    db.commit()
    db.refresh(db_computing)
    return db_computing
