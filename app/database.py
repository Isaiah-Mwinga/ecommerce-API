from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL= "postgresql+psycopg2://postgres:root@localhost/Item_db"
engine = create_engine(DATABASE_URL, 
                        echo=True)
                         
    

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()