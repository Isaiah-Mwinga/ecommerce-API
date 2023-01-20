from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.Computing import schemas, crud

router = APIRouter(tags=["Computing"], prefix="/computing")

@router.post("/computing/",status_code=status.HTTP_201_CREATED, response_model=schemas.Computing)
def create_computing(computing: schemas.Computing, db: Session = Depends(get_db)):
    if crud.get_computing_by_name(computing.name, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Computing already exists")
    return crud.create_computing(computing, db)

@router.get("/computing/all", status_code=status.HTTP_200_OK, response_model=list[schemas.Computing])
def get_all_computings(db: Session = Depends(get_db)):
    return crud.get_all_computings(db)

@router.get("/computing/{computing_id}", status_code=status.HTTP_200_OK, response_model=schemas.Computing)
def get_computing_by_id(computing_id: int, db: Session = Depends(get_db)):
    db_computing = crud.get_computing_by_id(computing_id, db)
    if not db_computing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Computing not found")
    return db_computing

@router.put("/computing/{computing_id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Computing)
def update_computing(computing_id: int, computing: schemas.Computing, db: Session = Depends(get_db)):
    db_computing = crud.get_computing_by_id(computing_id, db)
    if not db_computing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Computing not found")
    return crud.update_computing(computing_id, computing, db)

@router.delete("/computing/{computing_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_computing(computing_id: int, db: Session = Depends(get_db)):
    db_computing = crud.get_computing_by_id(computing_id, db)
    if not db_computing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Computing not found")
    crud.delete_computing(computing_id, db)