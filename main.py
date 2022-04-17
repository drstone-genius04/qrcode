# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://youtu.be/PIWB-e2GqFM"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("myyoutube.svg", scale=8)