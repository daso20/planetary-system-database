from sqlalchemy.orm import Session
from connection import engine
from models import Base

Base.metadata.create_all(engine)

#with Session(engine) as session:
#    
    
#    session.add_all([])
#    session.commit()