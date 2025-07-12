from typing import Optional
from pydantic import BaseModel, ConfigDict


class AuthorSchema(BaseModel):
    name: str
    age: int
    about: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class AuthorRead(BaseModel):
    id: int
    name: str
    age: int
    about: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
