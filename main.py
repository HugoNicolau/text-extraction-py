from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import pytesseract
import io

app = FastAPI()

@app.post("/extract-text")
@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))

        text = pytesseract.image_to_string(image)

        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")