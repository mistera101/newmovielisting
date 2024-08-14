from pydantic import BaseModel 
from typing import Optional, List

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    parent_id: Optional[int] = None

class Comment(CommentBase):
    id: int
    movie_id: int
    user_id: int
    parent_id: Optional[int] = None
    children: List['Comment'] = []

    class Config:
        orm_mode = True 
