from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Connect to a local SQLite file (it will be created automatically)
SQLALCHEMY_DATABASE_URL = "sqlite:///./patterns.db"

# 2. Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Create a session factory (this is how we read/write to the database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a base class for our database models
Base = declarative_base()

# Helper function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()