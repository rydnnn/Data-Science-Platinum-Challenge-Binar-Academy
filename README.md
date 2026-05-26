# 🧠 Gold Challenge — Hate Speech Detection API
### Binar Academy · Data Science Bootcamp

> REST API untuk deteksi hate speech dan konten abusif pada teks Twitter berbahasa Indonesia, dibangun dengan Flask dan didokumentasikan dengan Swagger UI.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-UI-85EA2D?style=flat&logo=swagger&logoColor=black)

---

## 📌 Tentang Project

Project ini merupakan **Gold Challenge** dari Binar Academy Data Science Bootcamp. Tujuannya adalah membangun REST API yang dapat memproses dan membersihkan teks tweet, sebagai bagian dari pipeline deteksi **hate speech** dan konten **abusif** berbahasa Indonesia.

Dataset yang digunakan berisi **13.044 tweet** yang telah dilabeli secara manual dengan kategori hate speech yang detail.

---

## ✨ Fitur

- 🔍 **Text Processing API** — Membersihkan teks dari karakter non-alfanumerik via endpoint POST
- 📚 **Swagger UI** — Dokumentasi API interaktif di `/docs/`
- 🗃️ **SQLite Database** — Dataset tersimpan dalam database lokal via `binar.db`
- 📊 **Dataset Export** — Script untuk mengimpor CSV ke SQLite

---

## 📊 Dataset

Dataset terdiri dari **13.044 tweet** berbahasa Indonesia dengan label berikut:

| Kolom          | Deskripsi                                  |
|----------------|--------------------------------------------|
| `Tweet`        | Isi tweet                                  |
| `HS`           | Hate Speech (0/1)                          |
| `Abusive`      | Konten abusif (0/1)                        |
| `HS_Individual`| Target individu                            |
| `HS_Group`     | Target kelompok                            |
| `HS_Religion`  | Berbasis agama                             |
| `HS_Race`      | Berbasis ras/etnis                         |
| `HS_Physical`  | Berbasis fisik                             |
| `HS_Gender`    | Berbasis gender                            |
| `HS_Other`     | Kategori lainnya                           |
| `HS_Weak`      | Intensitas rendah                          |
| `HS_Moderate`  | Intensitas sedang                          |
| `HS_Strong`    | Intensitas tinggi                          |

**Distribusi label:**
- Hate Speech: 5.518 (42.3%) vs Non-HS: 7.526 (57.7%)
- Abusive: 5.005 (38.4%) vs Non-Abusive: 8.039 (61.6%)

---

## 🛠️ Tech Stack

| Komponen     | Teknologi               |
|--------------|-------------------------|
| Web Framework| Flask                   |
| API Docs     | Flasgger (Swagger UI)   |
| Database     | SQLite 3                |
| Data Processing | Pandas               |
| Language     | Python 3.8+             |

---

## 🚀 Cara Instalasi & Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/[USERNAME]/Data_Science-GoldChallenge-Binar-Academy.git
cd Data_Science-GoldChallenge-Binar-Academy
```

### 2. Buat virtual environment

```bash
python -m venv venv

# Aktivasi (Windows)
venv\Scripts\activate

# Aktivasi (Mac/Linux)
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (Opsional) Import dataset ke database

Jalankan script ini jika ingin membuat ulang `binar.db` dari dataset CSV:

```bash
python eksport_db.py
```

### 5. Jalankan API

```bash
python app4.py
```

API akan berjalan di: `http://localhost:5000`  
Dokumentasi Swagger: `http://localhost:5000/docs/`

---

## 📡 API Endpoints

### `POST /text-processing`

Memproses dan membersihkan teks dari karakter non-alfanumerik.

**Request:**
```
Content-Type: multipart/form-data
Body: text = "Halo, apa kabar???"
```

**Response:**
```json
{
  "status_code": 200,
  "description": "Teks yang sudah diproses",
  "data": "Halo  apa kabar   "
}
```

---

## 📁 Struktur Project

```
GoldChallenge-Binar-Academy/
├── docs/
│   └── text_processing.yml   # Swagger spec untuk endpoint
├── app4.py                   # Flask app & API endpoints
├── eksport_db.py             # Script export CSV → SQLite
├── finish-data-set.csv       # Dataset tweet berlabel
├── binar.db                  # SQLite database (generated)
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 📄 Lisensi

Project ini dibuat untuk keperluan edukasi dalam program **Binar Academy Data Science Bootcamp**.

---

<p align="center">Dibuat dengan 🐍 Python & Flask · Binar Academy Gold Challenge</p>
