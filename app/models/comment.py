from sqlalchemy import Column, Integer, String, ForeignKey  # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    parent_id = Column(Integer, ForeignKey("comments.id"), nullable=True)

    movie = relationship("Movie", back_populates="comments")
    user = relationship("User", back_populates="comments")
    children = relationship("Comment", back_populates="parent", remote_side=[id])
    parent = relationship("Comment", back_populates="children", remote_side=[id]) 
