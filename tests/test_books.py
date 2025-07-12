import pytest
from httpx import AsyncClient, ASGITransport

from src import create_app


class TestBooks:
    @pytest.mark.asyncio
    async def test_all_books(self):
        app = create_app()
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://test"
        ) as ac:
            response = await ac.get("/books", follow_redirects=True)
            assert response.status_code == 200

            data = response.json()

            for d in data:
                assert "title" in d
                assert "author_id" in d
                assert type(d["title"]) is str
                assert type(d["author_id"]) is int

    @pytest.mark.asyncio
    async def test_new_book(self):
        app = create_app()
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://test"
        ) as ac:
            response = await ac.post("/books", json={
                "title": "Name",
                "author_id": 1,
            },
                                     follow_redirects=True)
            assert response.status_code == 200

            data = response.json()

            assert "message" in data
            assert "book_id" in data

    @pytest.mark.asyncio
    async def test_book_info(self):
        app = create_app()
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://test"
        ) as ac:
            response = await ac.get("/books/1", follow_redirects=True)
            assert response.status_code == 200

            data = response.json()

            assert "title" in data
            assert "author_id" in data
            assert "id" in data

            assert type(data["title"]) is str
            assert type(data["author_id"]) is int
            assert type(data["id"]) is int

    @pytest.mark.asyncio
    async def test_author_books(self):
        app = create_app()
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://test"
        ) as ac:
            response = await ac.get("/books/author/1", follow_redirects=True)
            assert response.status_code == 200

            data = response.json()

            for d in data:
                assert 'title' in d
                assert 'author_id' in d
                assert 'id' in d

                assert type(d["title"]) is str
                assert type(d["author_id"]) is int
                assert type(d["id"]) is int