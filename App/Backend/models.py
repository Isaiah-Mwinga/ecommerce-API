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

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    price = Column(float)

    owner = relationship("User", back_populates="items")    

class categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Item", back_populates="categories")

class computing(categories):
    __tablename__ = "computing"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Item", back_populates="computing")

class electronics(categories):
    __tablename__ = "electronics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Item", back_populates="electronics")

    class Gaming(categories):
        __tablename__ = "gaming"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="gaming")

    class Mobile(categories):
        __tablename__ = "mobile"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="mobile")
