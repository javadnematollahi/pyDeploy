## Image based API


In this example I write 5 API to make a users database.

You can add, update, read and delete your users which are stored in a sqlite database.

## How to use

run below command in terminal:

```
uvicorn main:app --reload
```

Then open postman and use below url with methodes are explained in below:

http://127.0.0.1:8000/


GET:

http://127.0.0.1:8000/users/

with this method you'll get all users in your database.

http://127.0.0.1:8000/users/{user_id}

with this method you can get a specifice user from database by its id.

POST:

http://127.0.0.1:8000/users

with this method you can create a new user in your database

you must enter below information as a form in Body when you send a request:

name: str
email: str


PUT:

http://127.0.0.1:8000/users/{user_id}

with this method you can update a user in your database

you must enter below information as a form in Body when you send a request:

name: str
email: str

and you must enter user id in url.

DELETE:

http://127.0.0.1:8000/users/{user_id}

with this method you can delete a user in your database

You must enter user id in url.


## How to install

```
pip install -r requirements.txt
```


