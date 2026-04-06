import wikipediaapi
import os

# Inisialisasi API (Gunakan User-Agent sesuai aturan Wikimedia)
wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="MyITBot/1.0 (contact: user@example.com)"
)

def save_category_articles(category_name, max_level=1):
    cat = wiki.page(f"Category:{category_name}")
    
    if not os.path.exists("wiki_it"):
        os.makedirs("wiki_it")

    print(f"Memproses Kategori: {category_name}")
    
    # Ambil semua artikel di dalam kategori ini
    for member in cat.categorymembers.values():
        if member.ns == wikipediaapi.Namespace.MAIN:
            # Ini adalah artikel (bukan kategori)
            file_path = f"wiki_it/{member.title.replace('/', '_')}.txt"
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(member.text)
                print(f"Saved: {member.title}")
        
        # Rekursif buat sub-kategori (batas level biar gak bengkak)
        elif member.ns == wikipediaapi.Namespace.CATEGORY and max_level > 0:
            save_category_articles(member.title.replace("Category:", ""), max_level - 1)

# Jalankan buat topik Jaringan
save_category_articles("Computer_networking", max_level=1)
