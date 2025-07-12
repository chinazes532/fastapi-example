from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Author
from sqlalchemy import select

from src.schemas.authors import AuthorSchema


class AuthorRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def set_author(self, creds: AuthorSchema):
        new_author = Author(
            name=creds.name,
            age=creds.age,
            about=creds.about
        )
        self.db.add(new_author)
        await self.db.commit()
        return new_author.id

    async def get_authors(self):
        result = await self.db.scalars(select(Author))
        return result.all()

    async def get_author(self, id: int):
        author = await self.db.scalar(select(Author).where(Author.id == id))
        return author
