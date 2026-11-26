from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentIn(BaseModel):
    """Data required to register a student."""

    student_id: str = Field(..., min_length=1, description="Unique student ID")
    full_name: str = Field(..., min_length=1, description="Student full name")
    email: EmailStr = Field(..., description="Student email address")
    department: str = Field(..., min_length=1, description="Department name")
    semester: int = Field(..., ge=1, le=12, description="Semester between 1 and 12")


class StudentUpdate(BaseModel):
    """Data for full update via PUT."""

    full_name: str = Field(..., min_length=1)
    email: EmailStr
    department: str = Field(..., min_length=1)
    semester: int = Field(..., ge=1, le=12)


class StudentPatch(BaseModel):
    """Data for partial update via PATCH."""

    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    semester: Optional[int] = Field(None, ge=1, le=12)


class Student(StudentIn):
    """Student data returned by the API."""

    pass
