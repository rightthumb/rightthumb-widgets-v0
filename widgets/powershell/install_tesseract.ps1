# Install Tesseract (UB Mannheim build) and Python deps
winget install -e --id UB-Mannheim.TesseractOCR
py -m pip install --upgrade pip pillow pytesseract

# Optional: set PATH immediately for the current session
$tez = "C:\Program Files\Tesseract-OCR"
if (Test-Path "$tez\tesseract.exe") { $env:Path = "$tez;$env:Path" }

# Quick sanity check
tesseract --version
