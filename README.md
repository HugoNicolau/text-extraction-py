# Text Extraction from Images using FastAPI and Tesseract

This project provides a simple API for extracting text from images using FastAPI and Tesseract OCR.

---

## Related Repositories

- [Frontend Repository (React + Vite + TypeScript)](https://github.com/HugoNicolau/text-extraction-react)


- [Backend Repository (NestJS + TypeScript)](https://github.com/HugoNicolau/text-extraction-nestjs)

- [Backend Repository (FastAPI + Python)](https://github.com/HugoNicolau/text-extraction-py)

---

## Features

- Upload an image and extract text using Tesseract OCR.
- FastAPI backend for handling image uploads and text extraction.
- Easy to set up and run locally.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- Tesseract OCR
- FastAPI
- Uvicorn
- Pillow
- Pytesseract

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HugoNicolau/text-extraction-py.git
   cd text-extraction-py
   ```

2. **Set up a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows: venv\Scripts\activate
    ```

    Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Install Tesseract OCR:**

    On Ubuntu/Debian:

    ```bash
    sudo apt-get install tesseract-ocr
    ```

    On macOS (using Homebrew):

    ```bash
    brew install tesseract
    ```

    On Windows, download the installer from Tesseract's GitHub page.

---

## Running the Project

1. **Start the FastAPI server:**

    ```bash
    uvicorn main:app --reload
    ```

    The server will start at http://localhost:8000.

2. **Test the API:**

    You can test the API using curl or a tool like Postman.

    Example using curl:

    ```bash
    curl -X POST -F "file=@/path/to/your/image.png" http://localhost:8000/extract-text/
    ```

    Example response:

    ```json
    {
      "text": "This is the extracted text from the image."
    }
    ```

---

## API Endpoints

### POST /extract-text/

Extract text from an uploaded image.

**Request:**

- File: The image file to process (supported formats: PNG, JPEG, etc.).

**Response:**

- text: The extracted text.

---

## Project Structure

```bash
text-extraction-py/
├── venv/                  # Virtual environment
├── main.py                # FastAPI application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Files to ignore in Git
└── image/                 # Folder for test images
    └── example-image.png
```

---

## Usage

1. **Upload an Image:**

    Use the /extract-text/ endpoint to upload an image and extract text.

2. **View Extracted Text:**

    The API will return the extracted text in JSON format.

---

## Example

Here’s an example of how to use the API with curl:

```bash
curl -X POST -F "file=@/path/to/your/image.png" http://localhost:8000/extract-text/
```

**Response:**

```json
{
  "text": "This is the extracted text from the image."
}
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the text extraction service.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text extraction.
- [Pillow](https://python-pillow.org/) for image processing.

---

## Contact

For questions or feedback, please reach out to me on [LinkedIn](https://www.linkedin.com/in/hugo-nicolau/) or via [email](mailto:nicolau.hugogiles@gmail.com).

---
