import os
from flask import Flask, render_template, request, send_file
import pandas as pd
from pdf2image import convert_from_path
import pytesseract
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Set correct Tesseract path (Windows users only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def pdf_to_excel(pdf_path, excel_path):
    """Converts PDF to Excel by extracting text using OCR."""
    images = convert_from_path(pdf_path, poppler_path=r"C:\poppler-24.08.0\Library\bin")
    extracted_data = []

    for image in images:
        text = pytesseract.image_to_string(image)
        lines = text.split("\n")
        
        for line in lines:
            if line.strip():
                extracted_data.append([line.strip()])  # Store each line

    df = pd.DataFrame(extracted_data, columns=["Extracted Data"])
    df.to_excel(excel_path, index=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf_file" not in request.files:
            return "No file uploaded", 400

        file = request.files["pdf_file"]
        if file.filename == "":
            return "No selected file", 400
        
        if not file.filename.lower().endswith(".pdf"):
            return "Invalid file type. Only PDFs are allowed.", 400

        filename = secure_filename(file.filename)
        pdf_path = os.path.join(UPLOAD_FOLDER, filename)
        excel_filename = os.path.splitext(filename)[0] + ".xlsx"
        excel_path = os.path.join(OUTPUT_FOLDER, excel_filename)
        file.save(pdf_path)

        pdf_to_excel(pdf_path, excel_path)
        
        return send_file(excel_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
