from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from decimal import Decimal

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
    equatorial_diameter: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    mass: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    semi_major_axis: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    orbital_period: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    inclination_to_suns_equator: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    orbital_eccentricity: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    rotation_period: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    confirmed_moons: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    axial_tilt: Mapped[Decimal] = mapped_column(Numeric(6,3))  
    rings: Mapped[str] = mapped_column(String(30))  
    atmosphere: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Planets(name={self.name!r}, planetary_system_id={self.planetary_system_id!r}, equatorial_diameter={self.equatorial_diameter!r}, mass={self.mass!r}, semi_major_axis={self.semi_major_axis!r}, orbital_period={self.orbital_period!r}, inclination_to_suns_equator={self.inclination_to_suns_equator!r}, orbital_eccentricity={self.orbital_eccentricity!r}, rotation_period={self.rotation_period!r}, confirmed_moons={self.confirmed_moons!r}, axial_tilt={self.axial_tilt!r}, rings={self.rings!r}, atmosphere={self.atmosphere!r})"
    
    def  attributes_as_list(self):
        return [self.name, self.planetary_system_id, str(self.equatorial_diameter), str(self.mass), str(self.semi_major_axis), str(self.orbital_period), str(self.inclination_to_suns_equator), str(self.orbital_eccentricity), str(self.rotation_period), str(self.confirmed_moons), str(self.axial_tilt), self.rings, self.atmosphere]
    