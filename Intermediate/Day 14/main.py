# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 14

# QR Code Generator
# This script requires the 'qrcode' and 'Pillow' libraries:
# pip install qrcode[pil]

import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    """
    Generates a QR code from the given data and saves it as an image file.
    """
    try:
        # Create a QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        img.save(filename)
        print(f"QR code generated and saved as {filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
data_to_encode = "https://github.com/kientech/365-Days-of-Python-Programming"
generate_qr_code(data_to_encode) 