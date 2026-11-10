from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, auth
from database import get_db

# Create a router for all auth-related endpoints
router = APIRouter(prefix="/auth", tags=["auth"])

# POST /auth/signup
@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Check if user already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Hash the password and create the user
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    
    # 3. Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# POST /auth/login
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    # 1. Find the user by email
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # 2. Verify the password
    if not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # 3. Generate a JWT token (their digital ID card)
    access_token = auth.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# GET /auth/me
@router.get("/me", response_model=schemas.User)
def get_current_user(current_user: models.User = Depends(auth.get_current_user)):
    # This endpoint uses the get_current_user function from auth.py 
    # to automatically check the token and return the user's info.
    return current_user