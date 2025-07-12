from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Book
from sqlalchemy import select

from src.schemas.books import BookSchema


class BookRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def set_book(self, creds: BookSchema):
        new_book = Book(
            title=creds.title,
            author_id=creds.author_id
        )
        self.db.add(new_book)
        await self.db.commit()
        return new_book.id

    async def get_books(self):
        books = await self.db.scalars(select(Book))
        return books.all()

    async def get_book_by_id(self, id: int):
        book = await self.db.scalar(select(Book).where(Book.id == id))
        return book

    async def get_author_books(self, author_id: int):
        books = await self.db.scalars(select(Book).where(Book.author_id == author_id))
        return books