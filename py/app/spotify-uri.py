import requests
from PIL import Image
from io import BytesIO

def generate_spotify_card(track_uri, template_path):
    # 1. Download Spotify Code (Warna Ijo #1DB954, BG Hitam #000000)
    api_url = f"https://scannables.scdn.co/v1/png/000000/1DB954/640/{track_uri}"
    response = requests.get(api_url)
    spotify_bar = Image.open(BytesIO(response.content))

    # 2. Buka Template Canva & Tempel
    card = Image.open(template_path)
    # Resize bar biar gak kegedean (misal lebar 400px)
    spotify_bar = spotify_bar.resize((400, int(spotify_bar.height * (400/spotify_bar.width))))
    
    # Tempel di koordinat X=100, Y=500 (sesuaikan ama desain Canva lu)
    card.paste(spotify_bar, (100, 500)) 
    
    card.save("hasil_kartu_nama.png")
    print("Mantap bre! Kartu nama udah jadi di hasil_kartu_nama.png")

# Cara pakenya:
generate_spotify_card("spotify:track:4cOdK2wGqyR7v3A90Ynsjr", "template_canva.png")