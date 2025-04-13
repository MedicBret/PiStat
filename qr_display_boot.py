#!/usr/bin/env python3
import os
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
SCANNED_FLAG = os.path.join(BASE_DIR, "scanned.flag")
QR_IMAGE_PATH = os.path.join(STATIC_DIR, "control_panel_qr.png")

def show_qr():
    window = tk.Tk()
    window.title("Scan QR to Access Control Panel")
    window.configure(bg="white")
    window.attributes("-fullscreen", True)
    window.bind("<Escape>", lambda e: window.destroy())

    if not os.path.exists(QR_IMAGE_PATH):
        logging.error("QR code not found at %s", QR_IMAGE_PATH)
        tk.Label(window, text="QR Code Not Found", font=("Helvetica", 16), bg="white").pack(pady=20)
    else:
        try:
            img = Image.open(QR_IMAGE_PATH)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            qr_img = ImageTk.PhotoImage(img)
            tk.Label(window, image=qr_img, bg="white").pack(pady=20)
            # Retain a reference to avoid garbage collection
            window.qr_img = qr_img
        except Exception as e:
            logging.error("Error loading QR image: %s", e)
            tk.Label(window, text="Error Loading QR Code", font=("Helvetica", 16), bg="white").pack(pady=20)

    tk.Label(window, text="Scan the QR Code to Launch Control Panel",
             font=("Helvetica", 12), bg="white").pack(pady=10)

    def check_for_scan():
        if os.path.exists(SCANNED_FLAG):
            logging.info("Scan detected, launching main application")
            try:
                os.remove(SCANNED_FLAG)  # Prevent duplicate launches
            except Exception as e:
                logging.error("Error removing scanned flag: %s", e)
            window.destroy()
            subprocess.Popen(["python3", os.path.join(BASE_DIR, "boot.py")])
        else:
            window.after(500, check_for_scan)  # Check more frequently for responsiveness

    check_for_scan()
    window.mainloop()

if __name__ == "__main__":
    show_qr()
