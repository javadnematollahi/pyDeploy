from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    unit: int | None = None


class Course(CourseBase):

    class Config:
        from_attributes = True


class StudentBase(BaseModel):
    firstname: str
    lastname: str
    average: float
    graduated: bool


class Student(StudentBase):

    class Config:
        from_attributes = True