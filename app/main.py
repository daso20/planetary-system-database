from sqlalchemy.orm import Session
from connection import engine
from models import Base, Planets
from utils import FormatCSVData

# Creates tables if they don't exist
Base.metadata.create_all(engine)

with Session(engine) as session:
    list_of_planets = FormatCSVData(r'''C:\Users\ds\Documents\Python Scripts\planetary-system-database''')

    for planet in list_of_planets[1:]:
        list_of_parameters = []

        session_object = Planets(*list_of_parameters)

        session.add(session_object)

    session.commit()