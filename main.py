from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import pytesseract
import io
import logging

app = FastAPI()
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


logging.basicConfig(level=logging.DEBUG)

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    logging.debug(f"Received file: {file.filename} with content type: {file.content_type}")
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        content = await file.read()
        logging.debug(f"File size: {len(content)} bytes")
        image = Image.open(io.BytesIO(content))
        text = pytesseract.image_to_string(image)
        logging.debug(f"Extracted text: {text}")
        return {"text": text}
    except Exception as e:
        logging.error(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
