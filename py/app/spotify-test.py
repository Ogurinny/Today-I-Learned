import requests
import random

# apina,aing ga mau langsung diaksih gitu aja anjir,susah kitu ambilnya
api = "https://scannables.scdn.co/uri/640/spotify:track:"
input_uri = input("Masukin ID Track-nya aja njing,jangan simulasi jadi sdm rendah ga bisa baca: ") # Pastiin ID aja njing,nanti kalo banyak merahnya mlaah nyalahin devnya kontol

response = requests.get(api + input_uri)

# mastiin kalo ada responna,jangan mikir ini sulap yah
if response.status_code == 200:
    png_name = f"spotify_code_{random.randint(1000,9999)}.png"
    
    # simpen filena
    with open(png_name, "wb") as f:
        f.write(response.content)
        
    print(f"yes yesir! File  {png_name} siap ready dipake amjayy awoawkoakw.")
else:
    print("Gagal uyy, keknya lu salah masukin idnya dah")