from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class PlanetarySystem(Base):
    __tablename__ = "planetary_system"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))    

class Planets(Base):
    __tablename__ = "planets"

    name: Mapped[str] = mapped_column(primary_key=True)
    equatorial_diameter: Mapped[str] = mapped_column(String(30))  
    mass: Mapped[str] = mapped_column(String(30))  
    semi_major_axis: Mapped[str] = mapped_column(String(30))  
    orbital_period: Mapped[str] = mapped_column(String(30))  
    inclination_to_suns_equator: Mapped[str] = mapped_column(String(30))  
    orbital_eccentricity: Mapped[str] = mapped_column(String(30))  
    rotation_period: Mapped[str] = mapped_column(String(30))  
    confirmed_moons: Mapped[str] = mapped_column(String(30))  
    axial_tilt: Mapped[str] = mapped_column(String(30))  
    rings: Mapped[str] = mapped_column(String(30))  
    atmosphere: Mapped[str] = mapped_column(String(30))  