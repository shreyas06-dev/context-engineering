from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
from database import get_db

# Create a router for all pattern-related endpoints
router = APIRouter(prefix="/patterns", tags=["patterns"])

# GET /patterns
@router.get("/", response_model=list[schemas.Pattern])
def list_patterns(db: Session = Depends(get_db)):
    return crud.get_patterns(db)

# POST /patterns
@router.post("/", response_model=schemas.Pattern)
def create_new_pattern(pattern: schemas.PatternCreate, db: Session = Depends(get_db)):
    return crud.create_pattern(db=db, pattern=pattern)