from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base
from app.Users import hashing


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)

    def __repr__(self):
        return f'{self.name}, {self.email}, {self.password}, {self.id}'
    
    def verify_password(self, password):
        return hashing.verify_password(password, self.password)