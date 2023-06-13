from typing import Union
from batik_model_predict import predict
from fastapi import FastAPI, UploadFile, File
from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post('/recognize')
async def recognize_image(image: UploadFile):
    """ Recognize the uploaded image """
    if "image" not in image.content_type:
        raise HTTPException(status_code=400, detail="File must be an image")
    img = Image.open(image.file)
    predicted_class, confidence = predict(img)
    return {
        "result": predicted_class,
        "confidence": str(confidence)
    }