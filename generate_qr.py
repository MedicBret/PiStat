#!/usr/bin/env python3
import qrcode
from PIL import Image
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
OUTPUT_QR = os.path.join(STATIC_DIR, "control_panel_qr.png")

def get_ip():
    # Hardcoded for PiStat AP mode
    return "192.168.4.1"

def generate_qr():
    ip = get_ip()
    url = f"http://{ip}:5000"
    logging.info("Generating QR code for: %s", url)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Add logo to the center if available
    logo_path = os.path.join(STATIC_DIR, "logo.png")
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path)
            basewidth = 60
            wpercent = (basewidth / float(logo.size[0]))
            hsize = int((float(logo.size[1]) * float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
            pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
            if logo.mode == 'RGBA':
                qr_img.paste(logo, pos, mask=logo)
            else:
                qr_img.paste(logo, pos)
        except Exception as e:
            logging.error("Error adding logo to QR code: %s", e)
    else:
        logging.warning("Logo not found at %s", logo_path)

    try:
        qr_img.save(OUTPUT_QR)
        logging.info("QR code with embedded logo saved to: %s", OUTPUT_QR)
    except Exception as e:
        logging.error("Error saving QR code: %s", e)

if __name__ == "__main__":
    generate_qr()
