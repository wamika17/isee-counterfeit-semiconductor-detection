# System Architecture

The iSEE system combines visual inspection and electrical characterization to determine the authenticity of semiconductor ICs.

## Overall Workflow

```
IC Under Test
      │
      ▼
Image Capture
      │
      ▼
OCR Verification
      │
      ▼
Electrical Testing
      │
      ▼
Feature Extraction
      │
      ▼
Machine Learning
      │
      ▼
Prediction
      │
      ▼
Dashboard
```

## Major Modules

- Hardware
- OCR
- Electrical Analysis
- Machine Learning
- Dashboard

Each module operates independently and contributes information to the final prediction.
