from typing import List

from fastapi import APIRouter, HTTPException

from src.db.database import SessionDep
from src.handlers.book_repository import BookRepository
from src.schemas.books import BookSchema, BookRead


router = APIRouter(
    tags=["📚 Книги"],
    prefix="/books"
)


@router.get("/", response_model=List[BookRead])
async def all_books(session: SessionDep):
    repo = BookRepository(session)
    books = await repo.get_books()
    if not books:
        raise HTTPException(status_code=404, detail="Книги не найдены")
    return books


@router.post("/")
async def new_book(creds: BookSchema, session: SessionDep):
    repo = BookRepository(session)
    book_id = await repo.set_book(creds)
    return {
        "message": "ok",
        "book_id": book_id
    }


@router.get("/{id}", response_model=BookRead)
async def book_info(id: int, session: SessionDep):
    repo = BookRepository(session)
    book = await repo.get_book_by_id(id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.get("/author/{author_id}", response_model=List[BookRead])
async def author_books(author_id: int, session: SessionDep):
    repo = BookRepository(session)
    books = await repo.get_author_books(author_id)
    if not books:
        raise HTTPException(status_code=404, detail="Книги не найдены")
    return books


