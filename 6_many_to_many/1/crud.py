from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user:  schemas.User, db_user):
    if user.name is not None:
        db_user.name = user.name 
    if user.email is not None:
        db_user.email = user.email
    db.commit()
    return db_user

def delete_user(db: Session, db_user):
    db.delete(db_user)
    db.commit()