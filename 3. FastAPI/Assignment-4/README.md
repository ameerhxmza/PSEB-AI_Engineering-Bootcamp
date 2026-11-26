# Student Course Registration API

A modular FastAPI CRUD API for managing student records and course registrations.
Student data is stored in memory, so it resets whenever the server restarts.

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
| GET | `/students/` | List students; optionally filter with `?department=Computer Science` or `?semester=4` |
| GET | `/students/count` | Count registered students |
| GET | `/students/{student_id}` | Get a student by ID |
| POST | `/students/` | Register a new student (201 response) |
| PUT | `/students/{student_id}` | Fully update a student |
| PATCH | `/students/{student_id}` | Partially update a student (e.g. change only semester) |
| DELETE | `/students/{student_id}` | Remove a student |

Student semesters must be between 1 and 12. Email addresses must be valid.
Duplicate student IDs or emails return 400 Bad Request, missing student IDs return 404 Not Found,
and invalid request data returns 422.

## Project structure

- `app/main.py` creates the FastAPI app and registers the router.
- `app/routes/students.py` implements the student CRUD and bonus endpoints.
- `app/schemas/student_schema.py` defines request and response models.
- `app/data/store.py` contains the in-memory student store.
