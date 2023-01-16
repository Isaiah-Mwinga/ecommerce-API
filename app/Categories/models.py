from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    #computings = relationship("Computing", back_populates="category")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"

#class Computing(Base):
#    __tablename__ = "computings"
#    id = Column(Integer, primary_key=True, index=True)
#    name = Column(String, unique=True, index=True)
#    category_id = Column(Integer, ForeignKey("categories.id, ondelete='CASCADE"))
#    category = relationship("Category", back_populates="Computing")
#
#    def __repr__(self):
#        return f"Computing(id={self.id}, name={self.name}, category_id={self.category_id})"