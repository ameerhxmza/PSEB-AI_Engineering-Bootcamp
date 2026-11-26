from typing import Dict

from app.schemas.book_schema import Book

books: Dict[int, Book] = {}


def new_id() -> int:
    """Generate the next available book ID."""
    return max(books, default=0) + 1
