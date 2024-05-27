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

![screencapture-127-0-0-1-8000-redoc-2024-05-27-22_46_34](https://github.com/javadnematollahi/pyDeploy/assets/86910174/66f46ea9-f0b7-431e-8f3a-7d2e04c9009d)



## How to install

```
pip install -r requirements.txt
```


