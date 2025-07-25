from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str | None] = mapped_column(String, nullable=True)

    repr_cols_num = 3
    repr_cols = ['id', 'username', 'email']