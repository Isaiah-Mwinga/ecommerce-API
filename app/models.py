from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    price = Column(Integer , index=True)

    owner = relationship("User", back_populates="items")    

    def __repr__(self):
        return f"Item(id={self.id}, title={self.title}, description={self.description}, price={self.price})"

class categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Item", back_populates="categories")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, description={self.description})"

