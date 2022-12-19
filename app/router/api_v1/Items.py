from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import Item
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("Item/", response_model=Item)
def create_item(item: Item , db: Session = Depends(get_db)):
    new_item = models.Item(
        title=item.title, 
        description=item.description, 
        price=item.price, 
        tax=item.tax)
    new_item = Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

@router.get("Items", response_model=Item)
def read_Item(token: str = Depends(oauth2_scheme) , db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(Item.id == item_id).all()
    return {Item.name: Item.description
            }

@router.get("Item/{item_id}", response_model=Item)
def read_Item(item_id: int , db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item            

@router.put(path="Item/{item_id}", response_model=Item)
def update_Item(item_id: int, item: Item , db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.title = item.title
    db_item.description = item.description
    db_item.price = item.price
    db_item.tax = item.tax
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete(path="Item/{item_id}", response_model=Item)
def delete_Item(item_id: int , db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item