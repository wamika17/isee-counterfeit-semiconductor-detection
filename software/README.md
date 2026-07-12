# Software

This folder contains the desktop software used to communicate with the hardware prototype, process acquired data, and display the results through an interactive dashboard.

The software receives electrical measurements from the Arduino Mega through serial communication, performs preliminary analysis, and presents the information in an easy-to-understand interface.

---

## Components

| File | Description |
|------|-------------|
| app.py | Flask web application |
| serial_reader.py | Reads serial data from Arduino |
| requirements.txt | Python dependencies |

---

## Workflow

Arduino Mega
↓
Serial Communication
↓
Python
↓
Data Processing
↓
Flask Dashboard
↓
Prediction Display

---

## Software Stack

- Python
- Flask
- PySerial
- NumPy
- OpenCV
- Tesseract OCR
- Scikit-learn
