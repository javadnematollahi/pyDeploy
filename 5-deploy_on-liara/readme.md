## sqlalchemy

sqlalchemy is a useful package that able us to work with different databases and It makes us unnecessary to use MySQL language to connect to database.


I use below link to learn how to use sqlalchemy:

https://fastapi.tiangolo.com/tutorial/sql-databases/


After I write my APIs with using fastapi, I mprovide a dockerfile to build a docker image for my code.

## How to build docker file

docker build -t < a name for your docker image: if you want write a tag for it too > .

## How run docker image

docker run -d --name < a name for container > -p 80:80 < name of your image that you choose when build your image >

## How to deploy in liara

1.first register on liara

For python script on liara
1. از قسمت پلتفرم، قسمت برنامه های آماده گزینه ی داکر را انتخاب میکنید.
2. make a new program
3. then you need to install nodejs in your system.
you can use snap to install it:      sudo snap install node --classic
4. then you need to install liara:     npm install -g @liara/cli
5. then you must go to your project root in you system and run this command:      liara deploy

For database on liara

1. In database part choose postgres database
2. make a new program
3. after ypur database ready from "how to connect" part in liara copy link connection and paste it in your python code


## result

You can use my postgres database with below url:

https://fastapi-deploy.liara.run/docs