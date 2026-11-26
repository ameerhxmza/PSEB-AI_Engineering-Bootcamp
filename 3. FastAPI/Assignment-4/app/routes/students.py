from typing import List, Optional

from fastapi import APIRouter, HTTPException, status

from app.data.store import students
from app.schemas.student_schema import (
    Student,
    StudentIn,
    StudentPatch,
    StudentUpdate,
)

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[Student])
def get_all_students(
    department: Optional[str] = None,
    semester: Optional[int] = None,
):
    results = list(students.values())

    if department is not None:
        results = [
            s for s in results if s.department.lower() == department.lower()
        ]

    if semester is not None:
        results = [s for s in results if s.semester == semester]

    return results


@router.get("/count")
def count_students():
    return {"total_students": len(students)}


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    return students[student_id]


@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student_in: StudentIn):
    # Check if student ID already exists
    if student_in.student_id in students:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student with this ID already exists",
        )

    # Check if email is already registered
    for existing in students.values():
        if existing.email.lower() == student_in.email.lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email address already registered",
            )

    student = Student(**student_in.model_dump())
    students[student.student_id] = student
    return student


@router.put("/{student_id}", response_model=Student)
def update_student(student_id: str, student_update: StudentUpdate):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    # Check email duplicate across other students
    for sid, existing in students.items():
        if (
            sid != student_id
            and existing.email.lower() == student_update.email.lower()
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email address already in use by another student",
            )

    updated_student = Student(
        student_id=student_id,
        **student_update.model_dump(),
    )
    students[student_id] = updated_student
    return updated_student


@router.patch("/{student_id}", response_model=Student)
def patch_student(student_id: str, student_patch: StudentPatch):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    current_data = students[student_id].model_dump()
    patch_data = student_patch.model_dump(exclude_unset=True)

    # Check email conflict if email is being updated
    if "email" in patch_data:
        new_email = patch_data["email"].lower()
        for sid, existing in students.items():
            if sid != student_id and existing.email.lower() == new_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email address already in use by another student",
                )

    current_data.update(patch_data)
    updated_student = Student(**current_data)
    students[student_id] = updated_student
    return updated_student


@router.delete("/{student_id}")
def delete_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    del students[student_id]
    return {"message": "Student deleted"}
