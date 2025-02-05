import os
from flask import Flask, render_template, request, send_file
import pandas as pd
import pdfplumber
import pytesseract
from pdf2image import convert_from_path

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Set Poppler path (Update to your actual path)
poppler_path = r"C:\poppler-24.08.0\Library\bin"

# Set Tesseract path (Windows users only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def pdf_to_excel(pdf_path, excel_path):
    extracted_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()  # Extract structured tables
            if tables:
                for table in tables:
                    extracted_data.extend(table)
            else:
                # If no tables detected, fall back to OCR
                image = convert_from_path(pdf_path, poppler_path=poppler_path)[0]
                text = pytesseract.image_to_string(image, config="--psm 6")
                lines = [line.split() for line in text.split("\n") if line.strip()]
                extracted_data.extend(lines)

    # Convert extracted data to DataFrame and save as Excel
    df = pd.DataFrame(extracted_data)
    df.to_excel(excel_path, index=False, header=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf_file" not in request.files:
            return "No file uploaded", 400

        file = request.files["pdf_file"]
        if file.filename == "":
            return "No selected file", 400

        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        excel_path = os.path.join(OUTPUT_FOLDER, file.filename.replace(".pdf", ".xlsx"))
        file.save(pdf_path)

        pdf_to_excel(pdf_path, excel_path)
        
        return send_file(excel_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
