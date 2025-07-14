import pytest_asyncio

from src import create_app


@pytest_asyncio.fixture(scope="function")
async def f_add_book():
    return "Asyncio Book", 1


@pytest_asyncio.fixture(scope="function")
async def f_create_app():
    app = create_app()
    return app


@pytest_asyncio.fixture(scope="function")
async def f_add_author():
    return "Ivan", 17, "B"

