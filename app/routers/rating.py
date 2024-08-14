from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from typing import List
from app.schemas.rating import Rating, RatingCreate
from app.models.rating import Rating as RatingModel
from app.models.movie import Movie as MovieModel
from app.database import SessionLocal
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal() 
