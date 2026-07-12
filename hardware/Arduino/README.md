# Arduino Firmware

This folder contains the firmware responsible for controlling the electrical testing hardware.

The firmware performs the following tasks:

- Generates logic input patterns.
- Reads digital outputs.
- Measures analog voltages.
- Sends measurement data through serial communication.
- Interfaces with the software dashboard.

---

## Planned Files

```
Arduino/

counterfeit_detector.ino
```

---

## Firmware Workflow

```
Initialize Pins
      ↓
Generate Logic Inputs
      ↓
Read IC Outputs
      ↓
Measure Voltage
      ↓
Transmit Data
      ↓
Repeat
```
