from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from app.database import Base, get_db
from app.config import settings


SQLALCHEMY_URL = f'postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.test_db_name}'
engine = create_engine(SQLALCHEMY_URL)
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    test_db = TestSession()
    try:
        yield test_db
    finally:
        test_db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
