import random

def test():
    barang = ("Roti", "Susu", "Gula", "Telur", "Mentega")
    brng_random = random.choice(barang)

    number = random.randint(1, 100)
    print(f"Barang yang dipilih: {brng_random}")
    print(f"Angka acak antara 1 dan 100: {number}")




test()