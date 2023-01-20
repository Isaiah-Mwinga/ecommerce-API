from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    computings = relationship("Computing", back_populates="Category")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"

