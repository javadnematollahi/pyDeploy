from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse, FileResponse, RedirectResponse
from typing import Union
import cv2
import numpy as np
import io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/salam/{firstname}/{surname}")
def salam(firstname: str, surname: str="nematollahi"):
    return {"message": f"Hello {firstname} {surname}"}

@app.get("/salam/{firstname}")
def salam1(firstname: str, surname: str="nematollahi"):
    return {"message": f"Hello {firstname} {surname}"}

@app.get("/tv-channel/{name}")
def test1(name: Union[str, int]):
    return {"name": name}

@app.get("/item/{item_id}")
async def root1(item_id):
    return {"message": f"Hello World {item_id}"}

@app.get("/create-image/{red}/{green}/{blue}")
def creat_image(red: int, green: int, blue:int):
    if 0<= red <= 255 and 0 <= green <= 255 and 0<= blue <= 255:
        image = np.zeros((300, 200, 3), dtype=np.uint8)
        image[:, :] = (red, green, blue)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite("image.jpg", image)
        _, encode_image = cv2.imencode(".png", image)

        return StreamingResponse(io.BytesIO(encode_image.tobytes()), media_type = "image/png")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="numbers must be between 0 and 255")
    
