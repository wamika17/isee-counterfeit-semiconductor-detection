# Hardware Design

This folder contains the embedded hardware implementation of the iSEE Counterfeit Semiconductor Detection System.

The hardware platform performs electrical characterization of semiconductor integrated circuits by applying predefined logic inputs, measuring output responses, and transmitting collected data to the software interface for further analysis.

---

## Hardware Overview

The prototype is designed around an Arduino Mega 2560 which acts as the central controller.

The Arduino generates digital test patterns, acquires analog voltage measurements, and communicates with the host computer through serial communication.

---

## Components Used

| Component | Function |
|-----------|----------|
| Arduino Mega 2560 | Main controller |
| 7400 NAND IC | Device Under Test (DUT) |
| LM324 Operational Amplifier | Signal conditioning |
| Breadboard | Prototype assembly |
| Jumper wires | Circuit connections |
| USB Cable | Serial communication |

---

## Pin Configuration

| Arduino Pin | Connection |
|-------------|------------|
| D2 | NAND Input A |
| D3 | NAND Input B |
| D4 | NAND Output |
| A0 | Input Voltage Measurement |
| A1 | Output Voltage Measurement |

---

## Hardware Workflow

1. Insert the IC into the test fixture.
2. Arduino generates logic input combinations.
3. Output voltage is measured.
4. Measurements are transmitted over Serial.
5. Software analyzes collected data.

---

## Folder Contents

```
hardware/
│
├── Arduino/
├── Circuit_Diagram.png
├── Prototype.jpg
└── README.md
```

---

## Future Improvements

- Dedicated PCB
- Automatic IC socket
- Multiple IC family support
- Higher precision ADC
