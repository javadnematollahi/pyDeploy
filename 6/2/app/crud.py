from sqlalchemy.orm import Session

from . import models, schemas


def get_student(db: Session, firstname: str):
    return db.query(models.Student).filter(models.Student.firstname == firstname).first()

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: schemas.Student):
    db_student = models.Student(firstname=student.firstname, lastname=student.lastname, average=student.average, graduated=student.graduated)
    db.add(db_student)
    student.model_dump()
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student:  schemas.Student, db_student):
    if student.firstname is not None:
        db_student.firstname = student.firstname 
    if student.lastname is not None:
        db_student.lastname = student.lastname 
    if student.average is not None:
        db_student.average = student.average 
    if student.graduated is not None:
        db_student.graduated = student.graduated
    db.commit()
    return db_student

def delete_student(db: Session, db_student):
    db.delete(db_student)
    db.commit()

def get_course(db: Session, name: str):
    return db.query(models.Course).filter(models.Course.name == name).first()

def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


def create_course(db: Session, course: schemas.Course):
    db_course = models.Course(name=course.name, unit=course.unit)
    db.add(db_course)
    course.model_dump()
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course:  schemas.Course, db_course):
    if course.name is not None:
        db_course.name = course.name 
    if course.unit is not None:
        db_course.unit = course.unit 
    db.commit()
    return db_course

def delete_course(db: Session, db_course):
    db.delete(db_course)
    db.commit()

def add_course_to_student(db: Session, student_id: int, course_id: int): # TODO: need fix
    student = db.query(models.Student).get(student_id)
    course = db.query(models.Course).get(course_id)
    
    student.courses.append(course)
    course.students.append(student)
    db.commit()