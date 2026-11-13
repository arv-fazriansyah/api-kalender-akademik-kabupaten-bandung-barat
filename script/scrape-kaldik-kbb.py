import json
import os
from datetime import datetime
import requests

DATA_DIR = "data"
AGENDA_DIR = os.path.join(DATA_DIR, "agenda")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(AGENDA_DIR, exist_ok=True)

# Data lengkap Kalender Pendidikan Kabupaten Bandung Barat (KBB)
# Termasuk 2026/2027, 2025/2026, dan 2024/2025
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
    },
    "2024-2025": {
        "tahun_ajaran": "2024/2025",
        "slug": "2024-2025",
        "status": "tersedia",
        "sumber": {
            "halaman": "https://disdikkbb.org/kalender-pendidikan-disdik-kab-bandung-barat-tahun-pelajaran-2024-2025/",
            "api": "https://disdikkbb.org/wp-json/wp/v2/posts?search=kalender%20pendidikan",
            "pembaruan_terakhir": "2024-08-08T06:39:09Z",
            "dibuat": "2024-07-14T20:17:51Z"
        },
        "dokumen": [
            {
                "halaman": "https://disdikkbb.org/kalender-pendidikan-disdik-kab-bandung-barat-tahun-pelajaran-2024-2025/",
                "url": "http://disdikkbb.org/wp-content/uploads/2024/07/KALDIK-KBB-FIX-2024-2025.pdf"
            }
        ],
        "agenda": [
            {
                "semester": 1,
                "mulai": "2024-07-15",
                "selesai": "2024-07-15",
                "kategori": "kegiatan",
                "agenda": "Hari pertama masuk sekolah",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-07-15",
                "selesai": "2024-07-20",
                "kategori": "kegiatan",
                "agenda": "Masa Pengenalan Lingkungan Sekolah (MPLS)",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-07-07",
                "selesai": "2024-07-07",
                "kategori": "libur",
                "agenda": "Libur Tahun Baru Islam 1446 H",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-08-14",
                "selesai": "2024-08-14",
                "kategori": "peringatan",
                "agenda": "Hari Pramuka dan Pertemuan Pramuka Pendidikan Khusus",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-08-17",
                "selesai": "2024-08-17",
                "kategori": "libur",
                "agenda": "Libur hari Proklamasi Kemerdekaan RI",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-09-09",
                "selesai": "2024-09-12",
                "kategori": "asesmen",
                "agenda": "Pelaksanaan Asesmen Nasional SMP dan Sederajat",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-09-16",
                "selesai": "2024-09-16",
                "kategori": "libur",
                "agenda": "Libur Maulid Nabi Muhammad SAW",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-10-28",
                "selesai": "2024-10-31",
                "kategori": "asesmen",
                "agenda": "Pelaksanaan Asesmen Nasional SD dan sederajat Tahap I",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-11-25",
                "selesai": "2024-11-25",
                "kategori": "peringatan",
                "agenda": "Hari Guru Nasional",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-12-02",
                "selesai": "2024-12-14",
                "kategori": "asesmen",
                "agenda": "Penilaian sumatif akhir semester 1",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-12-20",
                "selesai": "2024-12-21",
                "kategori": "rapor",
                "agenda": "Penetapan dan Pembagian rapor semester 1",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-12-25",
                "selesai": "2024-12-26",
                "kategori": "libur",
                "agenda": "Libur dan Cuti Bersama Hari Natal",
                "catatan": ""
            },
            {
                "semester": 1,
                "mulai": "2024-12-23",
                "selesai": "2025-01-04",
                "kategori": "libur",
                "agenda": "Libur semester 1",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-01-01",
                "selesai": "2025-01-01",
                "kategori": "libur",
                "agenda": "Libur Tahun Baru Masehi",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-01-06",
                "selesai": "2025-01-06",
                "kategori": "kegiatan",
                "agenda": "Hari pertama masuk sekolah semester 2",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-01-27",
                "selesai": "2025-01-29",
                "kategori": "libur",
                "agenda": "Prakiraan libur Isra Mi'raj & Tahun Baru Imlek",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-02-28",
                "selesai": "2025-03-02",
                "kategori": "libur",
                "agenda": "Prakiraan libur awal Ramadan 1446 H",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-04-01",
                "selesai": "2025-04-02",
                "kategori": "libur",
                "agenda": "Prakiraan Hari Raya Idulfitri 1446 H",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-05-01",
                "selesai": "2025-05-01",
                "kategori": "libur",
                "agenda": "Libur Hari Buruh",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-05-12",
                "selesai": "2025-05-12",
                "kategori": "libur",
                "agenda": "Libur Hari Raya Waisak",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-06-01",
                "selesai": "2025-06-01",
                "kategori": "libur",
                "agenda": "Libur Hari Lahir Pancasila",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-06-26",
                "selesai": "2025-06-27",
                "kategori": "rapor",
                "agenda": "Penetapan dan Pembagian rapor semester 2",
                "catatan": ""
            },
            {
                "semester": 2,
                "mulai": "2025-06-30",
                "selesai": "2025-07-12",
                "kategori": "libur",
                "agenda": "Libur Akhir Tahun Pelajaran",
                "catatan": ""
            }
        ],
        "penilaian_akhir": [],
        "catatan": [
            "Untuk tanggal penetapan rapor siswa akhir jenjang adalah pada tanggal dilaksanakan rapat penentuan kelulusan."
        ]
    }
}

def generate_api():
    waktu_sekarang = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    tahun_ajaran_list = []
    
    for slug, data in KBB_DATA.items():
        file_path = os.path.join(DATA_DIR, f"{slug}.json")
        data["diambil_pada"] = waktu_sekarang
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        tahun_ajaran_list.append({
            "slug": data["slug"],
            "tahun_ajaran": data["tahun_ajaran"],
            "status": data["status"],
            "file": f"data/{slug}.json",
            "jumlah_agenda": len(data["agenda"]),
            "jumlah_dokumen": len(data["dokumen"]),
            "pembaruan_terakhir": data["sumber"]["pembaruan_terakhir"]
        })
        
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
        
    print(f"Berhasil memperbarui data API lengkap di folder '{DATA_DIR}/'.")

if __name__ == "__main__":
    generate_api()
