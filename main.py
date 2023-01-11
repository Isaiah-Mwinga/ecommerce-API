import os   
from fastapi import FastAPI,APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import Session, engine, Base
from app import Users,auth
from app.Users import router
from app.auth import router


Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(router.router)
#app.include_router(Categories.router)
#app.include_router(Computing.router)
#app.include_router(auth.router)



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