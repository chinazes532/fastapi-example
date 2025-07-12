from typing import List

from fastapi import APIRouter, HTTPException

from src.db.database import SessionDep
from src.handlers.author_repository import AuthorRepository
from src.schemas.authors import AuthorSchema, AuthorRead


router = APIRouter(
    tags=["🙎‍♂️ Авторы"],
    prefix="/authors"
)


@router.get("/", response_model=List[AuthorRead])
async def all_authors(session: SessionDep):
    repo = AuthorRepository(session)
    authors = await repo.get_authors()
    if not authors:
        raise HTTPException(status_code=404, detail="Авторы не найдены")
    return authors


@router.post("/")
async def new_author(creds: AuthorSchema, session: SessionDep):
    if creds.age <= 0:
        raise HTTPException(status_code=500, detail="Введите корректный возраст!")
    repo = AuthorRepository(session)
    author_id = await repo.set_author(creds)
    return {
        "message": "ok",
        "author_id": author_id
    }


@router.get("/{id}", response_model=AuthorRead)
async def author_info(id: int, session: SessionDep):
    repo =  AuthorRepository(session)
    author = await repo.get_author(id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    return author



