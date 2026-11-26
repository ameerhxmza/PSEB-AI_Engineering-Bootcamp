from pydantic import BaseModel, Field


class BookIn(BaseModel):
    """Data received from the user."""

    title: str
    author: str
    year: int 


class Book(BookIn):
    """Book data returned by the API."""

    id: int
