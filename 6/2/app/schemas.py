from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    unit: int | None = None


class Course(CourseBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class StudentBase(BaseModel):
    firstname: str
    lastname: str
    average: float
    graduated: bool


class Student(StudentBase):
    id: int
    is_active: bool
    courses: list[Course] = []

    class Config:
        from_attributes = True