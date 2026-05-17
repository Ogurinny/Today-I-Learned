import os
import tkinter as tk

def ing():
      inn = ent.get()
      aj = os.popen(f"{inn}").read()
      out.delete("1.0", tk.END)
      out.insert(tk.END, aj)

root = tk.Tk()
root.title("Apa aja")
root.geometry("500x500")

sh = tk.Label(root, text="apa aja coba:")
sh.pack()

ent = tk.Entry(root, width=60)
ent.pack(pady=5)

btn = tk.Button(root, text="Jalanin", command=ing)
btn.pack(pady=20)

out = tk.Text(root, width=80, height=25)
out.pack()

root.mainloop()

