from typing import List, Optional

from fastapi import APIRouter, HTTPException, status

from app.data.store import books, new_id
from app.schemas.book_schema import Book, BookIn

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[Book])
def get_all_books(author: Optional[str] = None):
    if author is not None:
        return [
            book
            for book in books.values()
            if book.author.lower() == author.lower()
        ]
    return list(books.values())


@router.get("/count")
def count_books():
    return {"count": len(books)}


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return books[book_id]


@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookIn):
    book = Book(id=new_id(), **book_in.model_dump())
    books[book.id] = book
    return book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_in: BookIn):
    if book_id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    book = Book(id=book_id, **book_in.model_dump())
    books[book_id] = book
    return book


@router.delete("/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    del books[book_id]
    return {"message": "Book deleted"}
