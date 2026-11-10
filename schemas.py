from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class PatternCreate(BaseModel):
    title: str
    base_persona: str
    context_examples: str
    task_instruction: str
    tradeoffs: Optional[str] = None

class Pattern(PatternCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

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
