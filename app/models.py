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
    categories = relationship("categories", back_populates="user",
                              cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}), email={self.email}), password={self.password}, is_active={self.is_active})"

class categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="categories")
    

    def __repr__(self):
        return f"categories(id={self.id}, name={self.name}, description={self.description})"

        class Computing(Categories):
            __tablename__ = "computing"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("categories.id"))
        
            owner = relationship("categories", back_populates="computing")
        
            def __repr__(self):
                return f"Computing(id={self.id}, name={self.name}, description={self.description})"
