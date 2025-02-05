# PDF to Excel Converter

## Overview
This Flask-based web application extracts tables and text from PDF files and converts them into Excel format. It utilizes `pdfplumber` for structured table extraction and falls back to `Tesseract OCR` for scanned PDFs when necessary.

## Features
- Converts structured PDF tables into Excel format
- Uses `pdfplumber` for accurate table detection
- Falls back to OCR (`Tesseract`) for scanned documents
- Web-based interface for easy file uploads and downloads

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Poppler (for `pdf2image`)
- Tesseract OCR (for text extraction from images)

### Install Dependencies
```sh
pip install flask pandas pdf2image pytesseract pdfplumber openpyxl
```

### Configure Paths
#### Poppler Path (Windows)
Download and install Poppler from [Poppler for Windows](https://blog.alivate.com.au/poppler-windows/). Set the correct path in `poppler_path`:
```python
poppler_path = r"C:\path\to\poppler\bin"
```

#### Tesseract Path (Windows)
Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki). Set the correct path in `pytesseract.pytesseract.tesseract_cmd`:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Usage
1. Start the Flask app:
   ```sh
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. Upload a PDF file.
4. The converted Excel file will be automatically downloaded.

## Project Structure
```
project-folder/
│── app.py             # Flask application
│── templates/
│   └── index.html     # Web interface
│── uploads/           # Folder for uploaded PDFs
│── output/            # Folder for converted Excel files
│── README.md          # Project documentation
```

## Troubleshooting
- **Poppler not found?** Ensure Poppler is installed and its `bin` directory is added to your system `PATH`.
- **Tesseract error?** Check if Tesseract OCR is installed and configured correctly.
- **Extracted data appears in one row?** Some PDFs may require better OCR preprocessing. Try adjusting `--psm` settings in Tesseract.

## License
This project is open-source and available under the MIT License.

