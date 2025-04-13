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

Get Started

Clone the Repository
git clone https://github.com/yourusername/PiStat.git
cd PiStat

Generate the QR for Instructor Intereface
python3 generate_qr.py

Start the QR boot display
python3 qr_display_boot.py

Instructor opens the Control Panel:
Connect to Pi’s Wi-Fi (e.g., PiStat-AP)
Scan QR code or visit: http://192.168.4.1:5000

Student GUI launches after scan:
Displays “YOU, More Prepared Than Ever”
Selects test type (CHEM8+ or CG4+)
Progress bar simulates test time (~2 minutes)
Displays results with color-coded values

Project Structure
PiStat/
├── boot.py                # Main fullscreen student GUI
├── flask_server.py        # Instructor control panel web server
├── generate_qr.py         # Generates QR code with embedded logo
├── qr_display_boot.py     # Displays QR code and launches GUI after scan
├── profiles.py            # Test profiles by condition/severity
├── selection.json         # Selected profile/severity (updated via control panel)
├── results_history.json   # Recent simulated test results
├── static/
│   └── logo.png           # Logo image embedded in QR code and UI

🧪 Supported Profiles
Each profile has mild, moderate, and critical values for CHEM8+ and CG4+.
Trauma
DKA
TBI
Sepsis
ARDS
DIC
Crush Injury
Crush Syndrome
Modify or add profiles in profiles.py.

📈 Sample Output
Test	Parameter	Value	Flag
CG4+	pH	7.15	🔴 Low
CHEM8+	Glu	650	🔴 High

👨‍🏫 Use Cases
Paramedic and EMT training
Tactical or austere medicine simulation
Classroom scenarios with instructor-led diagnostics
Low-resource or field-based simulation environments

✍️ Author
Bret Mitchell
SOARescue.com
📍 Pennsylvania, USA

📜 License
This project is open for educational and non-commercial use.
For redistribution or commercial licensing, contact the author directly.
