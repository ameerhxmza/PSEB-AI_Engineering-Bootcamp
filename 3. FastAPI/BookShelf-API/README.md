# BookShelf API

A modular FastAPI CRUD API for managing books. Book data is stored in memory,
so it resets whenever the server restarts.

## Setup

From this directory, create and activate a virtual environment, then install
the dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the API from this directory:

```powershell
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to try the
endpoints.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | API status |
| GET | `/books/` | List books; optionally filter with `?author=Jane Austen` |
| GET | `/books/count` | Count stored books |
| GET | `/books/{book_id}` | Get a book |
| POST | `/books/` | Create a book (201 response) |
| PUT | `/books/{book_id}` | Replace a book |
| DELETE | `/books/{book_id}` | Delete a book |

Book years must be between 0 and 2100. Missing book IDs return 404, and
invalid request data returns 422.

## Project structure

- `app/main.py` creates the FastAPI app and registers the router.
- `app/api/routes/books.py` implements the book endpoints.
- `app/schemas/book.py` defines request and response models.
- `app/data/store.py` contains the in-memory store and ID generator.
