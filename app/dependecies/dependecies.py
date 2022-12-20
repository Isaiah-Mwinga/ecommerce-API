from sqlalchemy.orm import Session
from app.database import Sessionlocal

# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        