from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL= "postgresql+psycopg2://postgres:root@localhost/testdb"
engine = create_engine(DATABASE_URL)
                         
    

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

