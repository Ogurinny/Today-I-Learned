import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

class SpotifyCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify Code Generator - Roti Edition")
        self.root.geometry("500x600")
        self.root.configure(bg="#121212") # Warna dark mode Spotify

        # Label Judul
        tk.Label(root, text="Spotify Code Generator", font=("Arial", 18, "bold"), 
                 fg="#1DB954", bg="#121212").pack(pady=20)

        # Input Link
        tk.Label(root, text="Paste Link/URI (Lagu/Playlist/Artist):", 
                 fg="white", bg="#121212").pack()
        self.entry_link = tk.Entry(root, width=50, font=("Consolas", 10))
        self.entry_link.pack(pady=10)
        self.entry_link.insert(0, "spotify:track:4cOdK2wGqyR7v3A90Ynsjr")

        # Tombol Generate
        self.btn_gen = tk.Button(root, text="Generate Code", command=self.process_code,
                                 bg="#1DB954", fg="white", font=("Arial", 10, "bold"),
                                 padx=20, pady=5)
        self.btn_gen.pack(pady=10)

        # Area Preview Gambar
        self.preview_label = tk.Label(root, text="Preview bakal muncul di sini", 
                                      fg="#555555", bg="#121212", width=400, height=150)
        self.preview_label.pack(pady=20)

        # Tombol Save
        self.btn_save = tk.Button(root, text="Save PNG", command=self.save_image, 
                                  state=tk.DISABLED)
        self.btn_save.pack()

        self.current_img = None

    def process_code(self):
        raw_input = self.entry_link.get().strip()
        
        # 1. Konversi Link Browser ke URI jika user copas URL biasa
        if "https://open.spotify.com/track/ID1" in raw_input:
            parts = raw_input.split('/')
            type_media = parts[-2]
            id_media = parts[-1].split('?')[0] # Buang tracking ID (?si=...)
            uri = f"spotify:{type_media}:{id_media}"
        else:
            uri = raw_input

        # 2. Tembak rute /uri/ yang udah pasti berhasil (Resolusi HD 1638)
        url = f"https://scannables.scdn.co/uri/1638/{uri}"

        try:
            print(f"Nyomot dari rute sukses: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                img_data = Image.open(BytesIO(response.content))
                self.current_img = img_data 

                # Resize tipis-tipis buat tampilin di frame GUI Tkinter
                display_img = img_data.resize((400, 100))
                self.photo = ImageTk.PhotoImage(display_img)
                
                self.preview_label.config(image=self.photo, text="")
                self.btn_save.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", f"Server nolak (Status: {response.status_code}). Cek URI-nya lagi bre.")
        except Exception as e:
            messagebox.showerror("Error", f"Koneksi/Library bermasalah: {e}")
            
    def save_image(self):
        if self.current_img:
            filename = "spotify_code_output.png"
            self.current_img.save(filename)
            messagebox.showinfo("Sukses", f"File disimpen sebagai {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpotifyCodeApp(root)
    root.mainloop()