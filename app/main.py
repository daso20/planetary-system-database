from sqlalchemy.orm import Session
from connection import engine
from models import Base

# Creates tables if they don't exist
Base.metadata.create_all(engine)

with Session(engine) as session:
