## Image based API


In this example I write an API that get an image as input_file.

The image is given to a YOLO segmentation model and some objects is detected.

And In result an image is returned with detected objects.

## How to use

run below command in terminal:

```
uvicorn main:app --reload
```

Then open postman and use below url with POST method:

http://127.0.0.1:8000/object-detection

You should send a file ,too.

in Body part set KEY with input_file and change the type to file.
in Value part chose an image from your system to send.

## Result

input:



output:

