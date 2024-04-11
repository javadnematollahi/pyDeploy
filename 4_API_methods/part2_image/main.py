from ultralytics import YOLO
from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import numpy as np
import cv2
import io


app = FastAPI()

# Load a pretrained YOLO model (recommended for training)
model = YOLO('assets/yolov8n-seg.pt')



@app.post("/object-detection")
async def rgb2gray(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(syatus_code=415, detail="Unsupported file type")
    
    contents = await input_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image  = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

    result = model.predict(image)
    result = result[0]
    for i in range(len(result.boxes.xyxy)):
        if result.boxes.conf[i] > 0.7:
            print(result[0].names[int(result.boxes.cls[i])])
            bbox_tensor = result.boxes.xyxy[i]
            bbox_ndarray = bbox_tensor.cpu().detach().numpy().astype(int)
            x1, y1, x2, y2 = bbox_ndarray
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 4)
            cv2.putText(image,result[0].names[int(result.boxes.cls[i])] , (x1+5, y1+50), cv2.FONT_HERSHEY_SIMPLEX , 2, (255, 0, 0), 3, cv2.LINE_AA) 
    
    _, encoded_image = cv2.imencode(".png", image)
    image_bytes = encoded_image.tobytes()
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")