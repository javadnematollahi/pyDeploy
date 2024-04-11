# Authorization

## Part 0 => Run 5 sample apies which they need api-key


| Name  | Description | Docs|
| :-------------: | :-------------: | :-------------: |
| The One API  | The Lord Of The Rings  | https://the-one-api.dev/documentation  |
| IconFinder  | 	Find Icons |     https://developer.iconfinder.com/reference/overview-1  |
| Fal	  | Illusion Diffusion | https://fal.ai/models/illusion-diffusion/api  |
| D-ID	  | Text2Avatar  | https://docs.d-id.com/reference/overview-2  |
| PlantNet  | Plant Classification  | https://my.plantnet.org/doc/openapi  |

## Part 1 => Plant

In this part name of a plant is received and an illusion image is produced.
Then the produced image is given to plantnet api and then name of that plant is returned.

To produce image I use below api:

https://fal.ai/models/illusion-diffusion/api

To guess the name of the produced plant's image I use below api:

https://my.plantnet.org/doc/openapi

## part 2 => FastAPI

To be more familier with fastapi, fastapi helloworld example is run.

## part 3 => Requests module

I write a simple code to get different features of requests module

## part 4 => Find github followers and followings

I write another simple code that you can use it to find the number of your followers and followings


# How to run

## part 0

In this part I use notebook file so use below file.

authorization.ipynb

## part 1

run below command in terminal:

```
python3 plant.py --plant <Enter the name of a flower>
```

## part 2

run below command in terminal:

```
uvicorn helloworld_fastapi:app --reload
```

then enter below url in browser:

http://127.0.0.1:8000


## part 3

run below command in terminal:

```
python3 request_versionfinder.py
```
or

```
python request_versionfinder.py
```

## part 4

run below command in terminal:

```
python3 githubfollwer_counter.py --user <Enter a github username>
```
or
```
python githubfollwer_counter.py --user <Enter a github username>
```