



import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://youtu.be/PIWB-e2GqFM"

# Generate QR code
url = pyqrcode.create(s)

# Create and saved as myyoutube
url.svg("myyoutube.svg", scale=8)
