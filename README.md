# iSEE – AI-Powered Counterfeit Semiconductor Detection System

An intelligent hardware-software platform designed to identify counterfeit semiconductor integrated circuits (ICs) by combining optical inspection, electrical parameter analysis, and machine learning.

The system performs a two-stage verification process. First, Optical Character Recognition (OCR) verifies the package markings printed on an IC against expected manufacturer information. Second, the IC undergoes electrical characterization where logic behavior and voltage responses are analyzed to detect deviations from genuine components. The collected data is processed using machine learning techniques to classify the device as **Genuine** or **Counterfeit**.

---

## Problem Statement

Counterfeit semiconductor components have become a major concern across industries including aerospace, automotive, defense, healthcare, and consumer electronics. Fake ICs often exhibit degraded performance, reduced reliability, incorrect markings, or recycled packaging while appearing visually identical to genuine devices.

Traditional inspection methods require expensive laboratory equipment and trained personnel, making them inaccessible for educational institutions, small industries, and rapid field testing.

This project proposes a low-cost embedded solution capable of performing preliminary counterfeit detection using both visual inspection and electrical testing.

---

## Objectives

- Develop a portable counterfeit semiconductor detection platform.
- Verify IC package markings using Optical Character Recognition (OCR).
- Measure electrical characteristics of logic ICs.
- Analyze collected data using machine learning techniques.
- Display test results through an interactive software dashboard.
- Provide a scalable architecture for future industrial deployment.

---

## Key Features

- OCR-based IC marking verification
- Electrical property analysis
- Embedded hardware testing platform
- Arduino Mega based data acquisition
- Machine Learning based classification
- Flask-based monitoring dashboard
- Low-cost and portable architecture

---

## System Workflow

1. Insert the semiconductor IC into the testing platform.
2. Capture the package marking for OCR verification.
3. Compare extracted text with expected manufacturer information.
4. Apply predefined logic inputs to the IC.
5. Measure electrical outputs and voltage characteristics.
6. Transfer measured values to the software dashboard.
7. Process collected information using a machine learning model.
8. Display the final classification as **Genuine** or **Counterfeit**.

---

## System Architecture

```
                IC Under Test
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 OCR Verification          Electrical Testing
        │                           │
        ▼                           ▼
 Package Validation        Voltage & Logic Analysis
        │                           │
        └─────────────┬─────────────┘
                      ▼
             Machine Learning Model
                      ▼
           Genuine / Counterfeit
                      ▼
              Flask Dashboard
```

---

## Hardware Components

| Component | Purpose |
|-----------|----------|
| Arduino Mega 2560 | Main embedded controller |
| 7400 NAND IC | Device under test |
| LM324 Operational Amplifier | Signal conditioning |
| Breadboard | Prototype implementation |
| Jumper Wires | Circuit connections |
| USB Serial Communication | Data transfer to PC |

---

## Software Stack

- Arduino IDE
- Python
- Flask
- OpenCV
- Tesseract OCR
- Scikit-learn
- NumPy
- Matplotlib

---

## Project Structure

```
isee-counterfeit-semiconductor-detection/

├── docs/
├── hardware/
├── software/
├── dashboard/
├── machine-learning/
├── ocr/
├── images/
├── README.md
```

---

## Detection Methodology

### Stage 1 – Optical Verification

The package markings printed on the integrated circuit are captured and processed using Optical Character Recognition (OCR). Extracted text is compared with expected manufacturer information to identify inconsistencies in device markings.

### Stage 2 – Electrical Verification

The IC is subjected to predefined logic inputs while electrical outputs are monitored. Voltage measurements and logic responses are analyzed to determine whether the observed behavior matches that of an authentic component.

### Stage 3 – Machine Learning Classification

Features extracted from optical verification and electrical testing are combined and processed using a machine learning model to determine the authenticity of the semiconductor device.

---

## Future Improvements

- Support for multiple IC families
- FPGA-based electrical testing
- Automated image acquisition
- Cloud database integration
- Explainable AI for classification
- Mobile application support
- Industrial test fixture design

---

## Contributors

**Wamika Varada**

Electronics and Communication Engineering

Dayananda Sagar College of Engineering

---

## License

This project is released under the MIT License.
