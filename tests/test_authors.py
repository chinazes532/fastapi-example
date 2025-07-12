import pytest
from httpx import AsyncClient, ASGITransport

from src import create_app


class TestAuthors:
    @pytest.mark.asyncio
    async def test_all_authors(self):
        app = create_app()
        async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            response = await ac.get("/authors", follow_redirects=True)
            assert response.status_code == 200

            data = response.json()
            assert data != []

            for author in data:
                assert "id" in author
                assert "name" in author
                assert type(author["name"]) is str
                assert type(author["age"]) is int

    @pytest.mark.asyncio
    async def test_new_author(self):
        app = create_app()
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://test"
        ) as ac:
            response = await ac.post("/authors", json={
                "name": "Ivan",
                "age": 17,
                "about": "python backend dev",
            },
                                     follow_redirects=True)

            assert response.status_code == 200

            data = response.json()
            assert "author_id" in data
            assert isinstance(data["author_id"], int)
            assert data["message"].lower() == "ok"

    @pytest.mark.asyncio
    async def test_author_info(self):
        app = create_app()
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://test"
        ) as ac:
            response = await ac.get("/authors/1", follow_redirects=True)
            assert response.status_code == 200

            data = response.json()
            assert "id" in data
            assert "name" in data
            assert "age" in data
            assert "about" in data