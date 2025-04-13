# Changelog

All notable changes to this project will be documented in this file.  
This project adheres to [Semantic Versioning](https://semver.org/).

---

## [v1.0.0] - 2025-04-13

🎉 Initial Release of PiStat

### Added
- Student-facing touchscreen GUI (`boot.py`)
- Instructor control panel (`flask_server.py`)
- QR code generation and boot handler (`generate_qr.py`, `qr_display_boot.py`)
- Profiles for Trauma, DKA, TBI, Sepsis, ARDS, DIC, Crush Injury, Crush Syndrome
- Test types: CHEM8+ and CG4+ with mild, moderate, and critical severities
- Automatic history logging with color-coded lab ranges
- Static folder support for logo and QR image

### Notes
- Designed for Raspberry Pi 3B+/4B
- Recommended display: 3.5" or larger touchscreen
- Python 3.7+ with tkinter, flask, pillow, qrcode

---

