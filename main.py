import os   
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas import User, Item
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware


from app.models import User, Item
from app.database import Sessionlocal, engine, Base

from app.schemas import User, Item

Base.metadata.create_all(engine)



app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

 #to avoid csrftokenError



# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/Item/", response_model=Item)
def create_item(item: Item, db: Session = Depends(get_db)):
    new_item = Item(
        title=item.title, 
        description=item.description, 
        price=item.price, 
        tax=item.tax)
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item        

@app.get("/Items", response_model=Item)
def read_Item(token: str = Depends(oauth2_scheme)):
    return {Item.name: Item.description
            }


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(oauth2_scheme)):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

