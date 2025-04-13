# PiStat

**PiStat** is a Raspberry Pi-based medical simulation platform for EMS, paramedic, and austere medical training programs. It simulates CHEM8+ and CG4+ lab results based on user-selected clinical profiles and severity, offering a realistic diagnostic decision-making experience. The interface includes a touchscreen GUI for students and a QR-accessed control panel for instructors.

---

## 🚀 Features

- Fullscreen student GUI with real-time lab simulation
- Instructor control panel via QR code access
- Supports CHEM8+ and CG4+ test profiles
- Dozens of predefined clinical scenarios (e.g., Trauma, DKA, TBI)
- Color-coded abnormal values based on lab ranges
- Historical result logging and review
- Designed for use in both classroom and field simulation environments

---

## 📦 Requirements

- **Raspberry Pi** (3B+, 4B, or newer recommended)
- **Raspberry Pi OS 64-bit**
- **3.5" or larger touchscreen**
- **Python 3.7+**

### Python Libraries
Install with pip:
```bash
pip3 install flask pillow qrcode
