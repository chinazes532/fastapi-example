from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.routes.authors import router as author_router
from src.routes.books import router as book_router

from src.db.database import create_db



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    print("✅ App is enable...")
    yield
    print("❌ App is disable...")


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(author_router)
    app.include_router(book_router)

    return app