from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ecommerce.db import Base
from ecommerce.user import hashing


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)

    def __init__(self, name, password, email):
        self.name = name
        self.password = hashing.get_hashed_password(password)
        self.email = email

    def verify_password(self, password):
        return hashing.verify_password(password, self.password)