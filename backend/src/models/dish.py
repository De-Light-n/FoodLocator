from sqlalchemy import ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class Dish(Base):
    __tablename__ = "dish"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    price: Mapped[float] = mapped_column(Float)
    rating: Mapped[float] = mapped_column(Float)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), index=True)

    restaurant: Mapped["Restaurant"] = relationship("Restaurant", back_populates="menu") # type: ignore

    repr_cols_num = 5
    repr_cols = ['id', 'name', 'price', 'rating', 'restaurant_id']
  