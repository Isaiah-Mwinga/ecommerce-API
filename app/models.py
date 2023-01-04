from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, index=True, unique=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    items = relationship("Item", back_populates="User", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}), email={self.email}), password={self.password}, is_active={self.is_active})"

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    price = Column(Integer , index=True, nullable=False)
    tax = Column(Integer , index=True, nullable=False)

    User = relationship("User", back_populates="items")  
    categories = relationship("Categories", back_populates="items", cascade="all, delete-orphan")  

    def __repr__(self):
        return f"Item(id={self.id}, title={self.title}, description={self.description}, price={self.price})"

class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("items.id"))

    owner = relationship("Item", back_populates="categories")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, description={self.description})"

        class Computing(Categories):
            __tablename__ = "computing"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("categories.id"))
        
            owner = relationship("Categories", back_populates="computing")
        
            def __repr__(self):
                return f"Computing(id={self.id}, name={self.name}, description={self.description})"

        class Laptops(Computing):
            __tablename__ = "laptops"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("computing.id"))
        
            owner = relationship("Computing", back_populates="laptops")
        
            def __repr__(self):
                return f"Laptops(id={self.id}, name={self.name}, description={self.description})"
        
        class Computers(Computing):
            __tablename__ = "computers"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("computing.id"))

            owner = relationship("Computing", back_populates="computers")

            def __repr__(self):
                return f"Computers(id={self.id}, name={self.name}, description={self.description})"