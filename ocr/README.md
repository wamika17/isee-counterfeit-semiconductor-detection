# Optical Character Recognition (OCR)

This module verifies the package markings printed on semiconductor ICs using Optical Character Recognition (OCR).

Counterfeit components often contain incorrect fonts, inconsistent markings, altered manufacturer names, or mismatched part numbers. This module extracts the printed text from an IC package and compares it with expected information.

---

## Workflow

IC Image
↓
Image Preprocessing
↓
OCR (Tesseract)
↓
Extract Package Marking
↓
Database Comparison
↓
Verification Result

---

## Planned Files

```
ocr/

├── ocr_reader.py
├── preprocess.py
└── README.md
```

---

## Software Used

- OpenCV
- Tesseract OCR
- Python
