from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from geoalchemy2 import Geometry
from src.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    address: Mapped[str] = mapped_column(String)
    rating: Mapped[float | None] = mapped_column(Float, nullable=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    #location: Mapped[Geometry | None] = mapped_column(Geometry(geometry_type='POINT', srid=4326), nullable=True)
    
    menu: Mapped[list["Dish"]] = relationship("Dish", back_populates="restaurant", cascade="all, delete-orphan") # type: ignore

    repr_cols_num = 4
    repr_cols = ['id', 'name', 'address', 'rating']

  


    
