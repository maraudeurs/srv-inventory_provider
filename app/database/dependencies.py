from sqlalchemy.orm import Session
from database.database import SessionLocal

## database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

