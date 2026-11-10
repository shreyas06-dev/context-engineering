from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# Association table for the Many-to-Many relationship (Favorites)
favorites = Table(
    "favorites",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("pattern_id", Integer, ForeignKey("patterns.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # A user can have many favorite patterns
    favorites = relationship("Pattern", secondary=favorites, back_populates="favorited_by")

class Pattern(Base):
    __tablename__ = "patterns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    problem = Column(Text, nullable=False)
    technique = Column(Text, nullable=False)
    example = Column(Text, nullable=True)
    tradeoffs = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # A pattern can be favorited by many users
    favorited_by = relationship("User", secondary=favorites, back_populates="favorites")