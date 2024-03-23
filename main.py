import qrcode

# Webpage URL you want to convert into a QR code
url = 'https://www.youtube.com/@sosotips/?sub_confirmation=1'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance, with a transparent background
img = qr.make_image(fill_color="black", back_color="transparent")  # Set back_color to None for transparency

# Save the image to a file
img.save("website_qr_transparent.png")
