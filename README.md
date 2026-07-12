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

- Multi-modal counterfeit semiconductor detection
- OCR-based IC package marking verification
- Electrical truth table verification
- Voltage characteristic analysis
- Embedded Arduino Mega testing platform
- Feature extraction for machine learning
- Flask-based monitoring dashboard

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

The detection system combines **optical verification** and **electrical characterization** to improve counterfeit detection accuracy.

### Stage 1 – Optical Verification

The IC package is inspected using Optical Character Recognition (OCR). Manufacturer markings and part numbers are extracted and compared with expected information.

### Stage 2 – Electrical Characterization

The Arduino Mega applies predefined logic input combinations to the IC under test.

The system measures:

- Logic outputs
- Input voltage
- Output voltage

The measured values are compared with the expected electrical behavior of a genuine component.

### Stage 3 – Feature Extraction

Information collected from OCR and electrical testing is converted into numerical features, including:

- OCR confidence
- Truth table accuracy
- Average output voltage
- Voltage deviation
- Number of failed logic tests

### Stage 4 – Machine Learning

The extracted features are analyzed using a machine learning classifier to determine whether the IC is genuine or counterfeit.

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
