from typing import Annotated

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    about: Mapped[str] = mapped_column(String(500), nullable=True)


class Book(Base):
    __tablename__ = "books"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))