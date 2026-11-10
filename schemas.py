from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# --- Pattern Schemas ---
class PatternCreate(BaseModel):
    title: str
    problem: str
    technique: str
    example: Optional[str] = None
    tradeoffs: Optional[str] = None

class Pattern(PatternCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- User Schemas ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: str
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True