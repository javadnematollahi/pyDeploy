from fastapi import Depends, FastAPI, HTTPException, Form
from sqlalchemy.orm import Session

import crud ,models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@app.post("/tasks", response_model=schemas.Task)
def create_task(title: str = Form(), description: str = Form(), time: str = Form(), status: int = Form(), db: Session = Depends(get_db)):
    task= schemas.Task(id=0 , title=title, description=description, time=time, status=status)
    db_task = crud.get_task(db, title=task.title)
    if db_task:
        raise HTTPException(status_code=400, detail="title already registered")
    return crud.create_task(db=db, task=task)


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, title: str = Form(), description: str = Form(), time: str = Form(), status: int = Form(), db: Session = Depends(get_db)):
    task= schemas.Task(id=task_id, title=title, description=description, time=time, status=status)
    db_task = crud.get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    result = crud.update_task(db, task=task, db_task=db_task)
    return result

@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, db_task=db_task)
    return db_task