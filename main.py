import os   
from fastapi import FastAPI,APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import Session, engine, Base
from app import Users,auth
from app.Users import user
from app.auth import services
from app.Categories import categories
from app.Computing import Computing
from app.Laptops import Laptops
from app.Desktops import Desktops
from app.Datastorage import Datastorage
from fastapi.testclient import TestClient

Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(services.router)
app.include_router(user.router)
app.include_router(categories.router)
app.include_router(Computing.router)
app.include_router(Laptops.router)
app.include_router(Desktops.router)
app.include_router(Datastorage.router)


client = TestClient(app)

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)