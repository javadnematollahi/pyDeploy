## Image based API


In this example I write 16 API to make a student-course database.

You can add, update, read and delete student and course to student and course table respectivily.

I used below postgres docker for database:

docker pull postgres

and I ran it with below command:

docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=123456789 -e POSTGRES_USER=javad -e POSTGRES_DB=user_student -d postgres

## How to use

run below command in terminal:

```
uvicorn main:app --reload
```

Then open postman and use below url with methodes are explained in below:




## How to install

```
pip install -r requirements.txt
```


