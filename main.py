from fastapi import FastAPI 
from app.routers import auth, movie, rating, comment
from app.database import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(movie.router, prefix="/movies", tags=["movies"])
app.include_router(rating.router, prefix="/ratings", tags=["ratings"])
app.include_router(comment.router, prefix="/comments", tags=["comments"]) 
