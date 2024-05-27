from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, BOOLEAN
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), unique=True)
    lastname = Column(String(50))
    average = Column(Float)
    graduated = Column(BOOLEAN, default=0)

    courses = relationship("Course", back_populates="students", secondary='students_courses')


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), index=True)
    unit = Column(Integer, index=True)

    students = relationship("Student", back_populates="courses", secondary='students_courses')


class StudentCourse(Base):
    __tablename__ = "students_courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))