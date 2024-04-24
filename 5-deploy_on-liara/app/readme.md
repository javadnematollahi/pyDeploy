## Image based API


In this example I write 5 API to make a todo list.

You can add, update, read and delete your tasks which are stored in a sqlite database.

## How to use

run below command in terminal:

```
uvicorn main:app --reload
```

Then open postman and use below url with methodes are explained in below:

http://127.0.0.1:8000/


GET:

http://127.0.0.1:8000/tasks/

with this method you'll get all tasks in your database.

http://127.0.0.1:8000/tasks/{task_id}

with this method you can get a specifice task from database by its id.

POST:

http://127.0.0.1:8000/tasks

with this method you can create a new task in your database

you must enter below information as a form in Body when you send a request:

title: str
description: str
time: str  
status: int

PUT:

http://127.0.0.1:8000/tasks/{task_id}

with this method you can update a task in your database

you must enter below information as a form in Body when you send a request:

title: str
description: str
time: str  
status: int

and you must enter task id in url.

DELETE:

http://127.0.0.1:8000/tasks/{task_id}

with this method you can delete a task in your database

You must enter task id in url.


## How to install

```
pip install -r requirements.txt
```


