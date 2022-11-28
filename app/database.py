from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:root@localhost/testdb",
                          echo=True)
    
Base = declarative_base()

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

