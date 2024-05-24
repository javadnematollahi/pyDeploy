from fastapi import Depends, FastAPI, HTTPException, Form
from sqlalchemy.orm import Session
from typing import List
from . import crud ,models, schemas
from . import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.post("/students", response_model=schemas.Student)
def create_student(firstname: str = Form(), lastname: str = Form(), average: str = Form(), graduated: int = Form(), db: Session = Depends(get_db)):
    student= schemas.Student(id=0 , firstname=firstname, lastname=lastname, average=average, graduated=graduated)
    db_student = crud.get_student(db, title=student.title)
    if db_student:
        raise HTTPException(status_code=400, detail="title already registered")
    return crud.create_student(db=db, student=student)


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, firstname: str = Form(), lastname: str = Form(), average: str = Form(), graduated: int = Form(), db: Session = Depends(get_db)):
    student= schemas.Student(id=student_id, firstname=firstname, lastname=lastname, average=average, graduated=graduated)
    db_student = crud.get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    result = crud.update_student(db, student=student, db_student=db_student)
    return result

@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.delete_student(db, db_student=db_student)
    return db_student


@app.get("/courses/", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@app.post("/courses", response_model=schemas.Course)
def create_course(name: str = Form(), unit: int = Form(), db: Session = Depends(get_db)):
    course= schemas.Course(id=0 , name=name, unit=unit)
    db_course = crud.get_course(db, name=course.name)
    if db_course:
        raise HTTPException(status_code=400, detail="title already registered")
    return crud.create_course(db=db, course=course)


@app.get("/courses/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_id(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.put("/courses/{course_id}", response_model=schemas.Course)
def update_course(course_id: int, name: str = Form(), unit: int = Form(), db: Session = Depends(get_db)):
    course= schemas.Course(name=name, unit=unit)
    db_course = crud.get_course_by_id(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    result = crud.update_course(db, course=course, db_course=db_course)
    return result

@app.delete("/courses/{course_id}", response_model=schemas.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_id(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    crud.delete_course(db, db_course=db_course)
    return db_course

@app.get("/courses_of_student/{student_id}")
def read_course_of_student(student_id: int, db: Session = Depends(get_db)):
    courses = crud.get_courses_of_student(db, student_id=student_id)
    if courses is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return courses

@app.get("/students_of_course/{course_id}")
def read_student_of_course(course_id: int, db: Session = Depends(get_db)):
    students = crud.get_students_of_course(db, course_id=course_id)
    if students is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return students

@app.delete("/student_from_course/{student_id}-{course_id}")
def delete_student_from_course(course_id: int,student_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_id(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_student = crud.get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.remove_student_of_course(db, course_id=course_id, student_id=student_id)
    return f"{db_student.firstname} is removed from {db_course.name}"

@app.delete("/course_from_student/{course_id}-{student_id}")
def delete_course_from_student(course_id: int,student_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_id(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_student = crud.get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.remove_course_of_student(db, course_id=course_id, student_id=student_id)
    return f"{db_course.name} is removed from {db_student.firstname}"

@app.post("/student_to_course/{student_id}-{course_id}", response_model=schemas.Student)
def add_student_to_course(course_id: int,student_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_id(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_student = crud.get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.add_student_to_courses(db, course_id=course_id, student_id=student_id)
    return f"{db_student.firstname} is added to {db_course.name}"

@app.post("/course_to_student/{course_id}-{student_id}", response_model=schemas.Student)
def add_course_to_student(course_id: int,student_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_id(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_student = crud.get_student_by_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.add_course_to_student(db, course_id=course_id, student_id=student_id)
    return f"{db_student.firstname} is added to {db_course.name}"
