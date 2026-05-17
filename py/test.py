import tkinter as tk
import os

def jalan():
    ip = entry.get()  # ambil isi input

    hasil = os.popen(f"nmap {ip}").read()

    text.delete("1.0", tk.END)
    text.insert(tk.END, hasil)

root = tk.Tk()
root.title("Nmap GUI")
root.geometry("700x500")

# input IP
label = tk.Label(root, text="Masukkan IP:")
label.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# tombol scan
btn = tk.Button(root, text="Jalankan Scan", command=jalan)
btn.pack(pady=10)

# output
text = tk.Text(root, width=80, height=25)
text.pack()

root.mainloop()
