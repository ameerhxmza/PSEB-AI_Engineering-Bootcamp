from fastapi import FastAPI

from app.routes.books import router as books_router

app = FastAPI(
    title="BookShelf API",
    description="A modular Book Management API built with FastAPI",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "BookShelf API is running!",
        "docs": "/docs",
    }


app.include_router(books_router)
