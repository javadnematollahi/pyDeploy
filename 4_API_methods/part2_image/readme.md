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

![bicycle](https://github.com/javadnematollahi/pyDeploy/assets/86910174/29cf68b8-9402-414f-af52-3d07dbfab096)


output:

![newbi](https://github.com/javadnematollahi/pyDeploy/assets/86910174/02cff249-4c08-4ee8-977e-0fca22660a80)

