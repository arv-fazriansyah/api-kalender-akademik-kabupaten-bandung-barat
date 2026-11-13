import json
import os
from datetime import datetime
import requests

DATA_DIR = "data"
AGENDA_DIR = os.path.join(DATA_DIR, "agenda")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(AGENDA_DIR, exist_ok=True)

WORDPRESS_API_URL = "https://disdikkbb.org/wp-json/wp/v2/posts?search=kalender%20pendidikan&per_page=10"

def fetch_kalender_from_wp():
    print(f"Mengambil data dari WordPress API: {WORDPRESS_API_URL}")
    try:
        response = requests.get(WORDPRESS_API_URL, timeout=15)
        response.raise_for_status()
        posts = response.json()
        print(f"Berhasil mendapatkan {len(posts)} postingan dari Disdik KBB.")
        return posts
    except Exception as e:
        print(f"Gagal mengambil data dari WordPress API: {e}")
        return []

def generate_api():
    waktu_sekarang = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    posts = fetch_kalender_from_wp()
    
    tahun_ajaran_list = []
    
    for post in posts:
        title = post.get("title", {}).get("rendered", "")
        link = post.get("link", "")
        date = post.get("date", "")
        slug = post.get("slug", "")
        
        # Ekstrak tahun ajaran dari judul/slug (misal: 2026-2027)
        # Jika tidak ditemukan, gunakan slug atau tanggal post
        tahun_ajaran_slug = slug
        
        item_data = {
            "id": post.get("id"),
            "tahun_ajaran": title,
            "slug": slug,
            "status": "tersedia",
            "sumber": {
                "halaman": link,
                "api": WORDPRESS_API_URL,
                "pembaruan_terakhir": post.get("modified"),
                "dibuat": date
            },
            "konten_html": post.get("content", {}).get("rendered", ""),
            "diambil_pada": waktu_sekarang
        }
        
        # Simpan file detail JSON per postingan
        file_path = os.path.join(DATA_DIR, f"{slug}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(item_data, f, ensure_ascii=False, indent=2)
            
        tahun_ajaran_list.append({
            "slug": slug,
            "judul": title,
            "file": f"data/{slug}.json",
            "pembaruan_terakhir": post.get("modified")
        })
        
    # Buat indeks utama kalender.json
    indeks_data = {
        "sumber": {
            "halaman": "https://disdikkbb.org/",
            "api": WORDPRESS_API_URL
        },
        "diambil_pada": waktu_sekarang,
        "jumlah": len(tahun_ajaran_list),
        "postingan": tahun_ajaran_list
    }
    
    indeks_path = os.path.join(DATA_DIR, "kalender.json")
    with open(indeks_path, "w", encoding="utf-8") as f:
        json.dump(indeks_data, f, ensure_ascii=False, indent=2)
        
    print(f"Berhasil menghasilkan file JSON dinamis di folder '{DATA_DIR}/'.")

if __name__ == "__main__":
    generate_api()
