import qrcode
import random

ins = input("Enter the data to encode in the QR code: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(ins)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
image_name = f"qrcode_{random.randint(1000,9999)}.png"

img.save(image_name)
print(f"QR code generated and saved as {image_name}")