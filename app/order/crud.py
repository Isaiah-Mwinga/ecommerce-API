from fastapi import HTTPException, status
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.database import get_db
