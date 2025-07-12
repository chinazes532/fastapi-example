from typing import List

from fastapi import APIRouter

from src.db.database import SessionDep
from src.schemas.user import UserSchema
from src.handlers.user_repository import RepositoryUser


user = APIRouter(
    tags=["Пользователь"],
    prefix="/user"
)


@user.get("/test")
async def test():
    return {"status": "OK"}


@user.post("/")
async def new_user(creds: UserSchema, session: SessionDep):
    repo = RepositoryUser(session)
    user_id = await repo.set_user(creds)

    return {"message": "User in created",
            "user_id": user_id}


@user.get("/", response_model=List[UserSchema])
async def all_users(session: SessionDep):
    repo = RepositoryUser(session)
    users = await repo.get_users()
    return users


@user.get("/{id}")
async def one_user(id: int, session: SessionDep):
    repo = RepositoryUser(session)
    user_info = await repo.get_user(id)
    return user_info
