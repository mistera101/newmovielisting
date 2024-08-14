from sqlalchemy import Column, Integer, String, Boolean 
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    movies = relationship("Movie", back_populates="owner")
    ratings = relationship("Rating", back_populates="user")
    comments = relationship("Comment", back_populates="user") 
