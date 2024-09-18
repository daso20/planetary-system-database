from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class PlanetarySystem(Base):
    __tablename__ = "planetary_systems"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"

class Planets(Base):
    __tablename__ = "planets"

    name: Mapped[str] = mapped_column(primary_key=True)
    planetary_system_id: Mapped[int] = mapped_column(ForeignKey("planetary_systems.id"))
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

    def __repr__(self) -> str:
        return f"Planets(name={self.name!r}, planetary_system_id={self.planetary_system_id!r}, equatorial_diameter={self.equatorial_diameter!r}, mass={self.mass!r}, semi_major_axis={self.semi_major_axis!r}, orbital_period={self.orbital_period!r}, inclination_to_suns_equator={self.inclination_to_suns_equator!r}, orbital_eccentricity={self.orbital_eccentricity!r}, rotation_period={self.rotation_period!r}, confirmed_moons={self.confirmed_moons!r}, axial_tilt={self.axial_tilt!r}, rings={self.rings!r}, atmosphere={self.atmosphere!r})"
    
    def  attributes_as_list(self):
        return [self.name, self.planetary_system_id, self.equatorial_diameter, self.mass, self.semi_major_axis, self.orbital_period, self.inclination_to_suns_equator, self.orbital_eccentricity, self.rotation_period, self.confirmed_moons, self.axial_tilt, self.rings, self.atmosphere]
    