from fastapi import FastAPI

from app.routes.students import router as students_router

app = FastAPI(
    title="Student Course Registration API",
    description="A modular Student Course Registration API built with FastAPI",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Student Course Registration API is running!",
        "docs": "/docs",
    }


app.include_router(students_router)
