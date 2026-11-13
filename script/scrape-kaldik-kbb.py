import json
import os
from datetime import datetime
import requests

# Konfigurasi Direktori
DATA_DIR = "data"
AGENDA_DIR = os.path.join(DATA_DIR, "agenda")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(AGENDA_DIR, exist_ok=True)

# Data Kurasi Agenda & Dokumen Kaldik Kabupaten Bandung Barat (KBB)
# Sesuai data resmi dari disdikkbb.org
KBB_DATA = {
    "2026-2027": {
        "tahun_ajaran": "2026/2027",
        "slug": "2026-2027",
        "status": "tersedia",
        "sumber": {
            "halaman": "https://disdikkbb.org/disdik-kbb-terbitkan-kalender-pendidikan-tahun-pelajaran-2026-2027/",
            "api": "https://disdikkbb.org/wp-json/wp/v2/posts?search=kalender%20pendidikan",
            "pembaruan_terakhir": "2026-07-05T11:07:59Z",
            "dibuat": "2026-07-05T00:00:00Z"
        },
        "dokumen": [
            {
                "halaman": "https://disdikkbb.org/disdik-kbb-terbitkan-kalender-pendidikan-tahun-pelajaran-2026-2027/",
                "url": "https://drive.google.com/drive/folders/1lemsBgEgwk1Ron9B9WoLhjvaVw3zhWlM?usp=sharing"
            }
        ],
        "agenda": [
            {
                "semester": 1,
                "mulai": "2026-07-13",
                "selesai": "2026-07-13",
                "kategori": "kegiatan",
                "agenda": "Hari pertama masuk sekolah Semester 1",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2026-07-13",
                "selesai": "2026-07-17",
                "kategori": "kegiatan",
                "agenda": "Masa Pengenalan Lingkungan Sekolah (MPLS) - Bagian 1",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2026-07-20",
                "selesai": "2026-07-21",
                "kategori": "kegiatan",
                "agenda": "Masa Pengenalan Lingkungan Sekolah (MPLS) - Bagian 2",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2026-08-03",
                "selesai": "2026-08-31",
                "kategori": "asesmen",
                "agenda": "Pelaksanaan Survei Lingkungan Belajar bagi Kepala Satuan Pendidikan dan Pendidik (PAUD, SD, SMP)",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2026-12-23",
                "selesai": "2026-12-23",
                "kategori": "rapor",
                "agenda": "Penetapan dan Pembagian Rapor Semester 1",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2026-12-28",
                "selesai": "2027-01-08",
                "kategori": "libur",
                "agenda": "Perkiraan libur Semester 1",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2027-01-11",
                "selesai": "2027-01-11",
                "kategori": "kegiatan",
                "agenda": "Hari pertama masuk sekolah Semester 2",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2027-02-08",
                "selesai": "2027-02-12",
                "kategori": "libur",
                "agenda": "Perkiraan libur awal Ramadan 1448 H",
                "catatan": "Menyesuaikan penetapan pemerintah"
            },
            {
                "semester": 2,
                "mulai": "2027-03-08",
                "selesai": "2027-03-19",
                "kategori": "libur",
                "agenda": "Perkiraan libur Idulfitri 1448 H",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2027-06-25",
                "selesai": "2027-06-25",
                "kategori": "rapor",
                "agenda": "Penetapan dan Pembagian Rapor Semester 2",
                "catatan": "Kelas akhir menyesuaikan rapat kelulusan"
            },
            {
                "semester": 2,
                "mulai": "2027-06-28",
                "selesai": "2027-07-09",
                "kategori": "libur",
                "agenda": "Libur akhir tahun ajaran",
                "catatan": ""
            }
        ],
        "penilaian_akhir": [],
        "catatan": [
            "Kepastian libur awal Ramadan menyesuaikan dengan penetapan awal Ramadan 1448 H oleh pemerintah.",
            "Khusus bagi peserta didik kelas akhir, penetapan rapor Semester 2 dilaksanakan pada tanggal rapat penentuan kelulusan satuan pendidikan."
        ]
    },
    "2025-2026": {
        "tahun_ajaran": "2025/2026",
        "slug": "2025-2026",
        "status": "tersedia",
        "sumber": {
            "halaman": "https://disdikkbb.org/kalender-pendidikan-tahun-pelajaran-2025-2026/",
            "api": "https://disdikkbb.org/wp-json/wp/v2/posts?search=kalender%20pendidikan",
            "pembaruan_terakhir": "2025-07-26T07:10:55Z",
            "dibuat": "2025-07-23T19:51:18Z"
        },
        "dokumen": [
            {
                "halaman": "https://disdikkbb.org/kalender-pendidikan-tahun-pelajaran-2025-2026/",
                "url": "https://drive.google.com/file/d/1kFqw_rD_mFlnUWBqi1GsSum7jnLFqzEj/view?usp=sharing"
            }
        ],
        "agenda": [
            {
                "semester": 1,
                "mulai": "2025-07-14",
                "selesai": "2025-07-14",
                "kategori": "kegiatan",
                "agenda": "Hari Pertama Masuk Sekolah Tahun Pelajaran 2025/2026",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2025-12-22",
                "selesai": "2026-01-02",
                "kategori": "libur",
                "agenda": "Libur Semester 1",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2026-01-05",
                "selesai": "2026-01-05",
                "kategori": "kegiatan",
                "agenda": "Hari Pertama Masuk Sekolah Semester 2",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2026-06-29",
                "selesai": "2026-07-10",
                "kategori": "libur",
                "agenda": "Libur Akhir Tahun Pelajaran",
                "catatan": ""
            }
        ],
        "penilaian_akhir": [],
        "catatan": [
            "Disusun berdasarkan pedoman Dinas Pendidikan Provinsi Jawa Barat dan Edaran Disdik KBB."
        ]
    }
}

def generate_api():
    waktu_sekarang = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    tahun_ajaran_list = []
    
    for slug, data in KBB_DATA.items():
        # Simpan file detail per tahun ajaran
        file_path = os.path.join(DATA_DIR, f"{slug}.json")
        data["diambil_pada"] = waktu_sekarang
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        # Tambahkan ke indeks kalender.json
        tahun_ajaran_list.append({
            "slug": data["slug"],
            "tahun_ajaran": data["tahun_ajaran"],
            "status": data["status"],
            "file": f"data/{slug}.json",
            "jumlah_agenda": len(data["agenda"]),
            "jumlah_dokumen": len(data["dokumen"]),
            "pembaruan_terakhir": data["sumber"]["pembaruan_terakhir"]
        })
        
    # Buat indeks kalender.json
    indeks_data = {
        "sumber": {
            "halaman": "https://disdikkbb.org/",
            "api": "https://disdikkbb.org/wp-json/wp/v2/posts"
        },
        "diambil_pada": waktu_sekarang,
        "jumlah": len(tahun_ajaran_list),
        "tahun_ajaran": tahun_ajaran_list
    }
    
    indeks_path = os.path.join(DATA_DIR, "kalender.json")
    with open(indeks_path, "w", encoding="utf-8") as f:
        json.dump(indeks_data, f, ensure_ascii=False, indent=2)
        
    print(f"Berhasil menghasilkan file JSON API Kalender Pendidikan KBB di folder '{DATA_DIR}/'.")

if __name__ == "__main__":
    generate_api()
