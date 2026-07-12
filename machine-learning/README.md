
# Machine Learning

This module classifies semiconductor ICs as **Genuine** or **Counterfeit** using features extracted from optical and electrical verification.

Unlike image-only classification, this approach combines multiple engineering parameters to improve reliability.

---

## Input Features

- OCR Confidence
- Truth Table Accuracy
- Average Input Voltage
- Average Output Voltage
- Voltage Drop
- Failed Logic Tests

---

## Workflow

Feature Extraction
↓
Dataset Generation
↓
Model Training
↓
Prediction
↓
Classification Result

---

## Planned Files

machine-learning/

├── dataset.csv
├── train_model.py
├── predict.py
└── README.md

---

## Machine Learning Algorithm

The current implementation demonstrates a Decision Tree classifier for binary classification.

Future versions can be extended to Random Forest, XGBoost, or Neural Networks.
