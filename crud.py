from sqlalchemy.orm import Session
import models
import schemas

def get_patterns(db: Session):
    # Read: Get all patterns from the database
    return db.query(models.Pattern).all()

def create_pattern(db: Session, pattern: schemas.PatternCreate):
    # Create: Turn the Pydantic schema into a SQLAlchemy model and save it
    db_pattern = models.Pattern(
        title=pattern.title,
        problem=pattern.problem,
        technique=pattern.technique,
        example=pattern.example,
        tradeoffs=pattern.tradeoffs
    )
    db.add(db_pattern)
    db.commit()       # Save to the database
    db.refresh(db_pattern) # Get the new ID and created_at from the database
    return db_pattern