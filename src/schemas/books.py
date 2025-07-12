from pydantic import BaseModel, ConfigDict


class BookSchema(BaseModel):
    title: str
    author_id: int

    model_config = ConfigDict(from_attributes=True)


class BookRead(BookSchema):
    id: int
    title: str
    author_id: int

    model_config = ConfigDict(from_attributes=True)