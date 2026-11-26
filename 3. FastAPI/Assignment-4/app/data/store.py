from typing import Dict

from app.schemas.student_schema import Student

# In-memory dictionary to store students keyed by student_id
students: Dict[str, Student] = {
    "101": Student(
        student_id="101",
        full_name="Ameer Hamza",
        email="ameer@university.edu",
        department="Computer Science",
        semester=4,
    ),
    "102": Student(
        student_id="102",
        full_name="Bilal Nadeem",
        email="bilal@university.edu",
        department="Data Science",
        semester=6,
    ),
}
