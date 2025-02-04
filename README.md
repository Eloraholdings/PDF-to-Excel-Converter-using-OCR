# PDF-to-Excel-Converter-using-OCR

## 📌 Overview
This is a **Flask web application** that converts **scanned PDFs** into **Excel files** using OCR (Optical Character Recognition). The app extracts text from PDF images using `pytesseract` and saves the structured data in an Excel file.

## 🚀 Features
- **Upload PDFs** via a web interface
- **Extract text** from scanned PDFs using OCR
- **Automatically download** the converted Excel file
- **User-friendly UI** with HTML & CSS
- Works on **Windows, macOS, and Linux**

## 🛠️ Installation
### 1️⃣ Install Required Dependencies
```bash
pip install flask pdf2image pytesseract pandas openpyxl
```

### 2️⃣ Install Tesseract OCR
- **Windows**: [Download & Install](https://github.com/UB-Mannheim/tesseract/wiki)
- **Linux**: `sudo apt install tesseract-ocr`
- **macOS**: `brew install tesseract`

### 3️⃣ Clone or Download the Repository
```bash
git clone https://github.com/kelvin-kahuho/pdf-to-excel-ocr.git
cd pdf-to-excel-ocr
```

## 📂 Project Structure
```
pdf_to_excel_app/
│── static/
│   └── styles.css   # CSS styling
│── templates/
│   └── index.html   # HTML frontend
│── uploads/         # Folder for uploaded PDFs (auto-created)
│── output/          # Folder for converted Excel files (auto-created)
│── app.py           # Flask backend script
│── README.md        # Project documentation
```

## 🏃‍♂️ Running the App
```bash
python app.py
```
Then, open **http://127.0.0.1:5000/** in your browser.

## 📸 Screenshots
| Upload PDF | Convert & Download |
|------------|-------------------|
| ![Upload](screenshots/upload.png) | ![Download](screenshots/download.png) |

## 🤝 Contributing
Feel free to contribute by submitting issues or pull requests.

## 📜 License
This project is licensed under the MIT License.

