from sqlalchemy.orm import Session

from . import models, schemas


def get_task(db: Session, title: str):
    return db.query(models.Task).filter(models.Task.title == title).first()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(title=task.title, description=task.description, time=task.time, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task:  schemas.Task, db_task):
    if task.title is not None:
        db_task.title = task.title 
    if task.description is not None:
        db_task.description = task.description 
    if task.time is not None:
        db_task.time = task.time 
    if task.status is not None:
        db_task.status = task.status
    db.commit()
    return db_task

def delete_task(db: Session, db_task):
    db.delete(db_task)
    db.commit()