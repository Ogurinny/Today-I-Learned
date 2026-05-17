import qrcode
import random
import tkinter as tk


def ing():
      inn = ent.get()
      qr = qrcode.QRCode(version=1, box_size=10, border=5)
      qr.add_data(inn)
      qr.make(fit=True)
      img = qr.make_image(fill='black', back_color='white')
      image_name = f"qrcode_{random.randint(1000,9999)}.png"
      img.save(image_name)
      out.delete("1.0", tk.END)
      out.insert(tk.END, f"QR code generated! Check the folder for the image file: {image_name}")

root = tk.Tk()
root.title("Testing qr code")
root.geometry("500x500")

sh = tk.Label(root, text="Data yang mau di encode apa dulu hayo:")
sh.pack()

ent = tk.Entry(root, width=60)
ent.pack(pady=5)

btn = tk.Button(root, text="Jalanin", command=ing)
btn.pack(pady=20)

out = tk.Text(root, width=80, height=25)
out.pack()

root.mainloop()

