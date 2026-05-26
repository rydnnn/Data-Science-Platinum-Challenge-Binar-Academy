# 🤖 Platinum Challenge — Tweet Sentiment Analysis API
### Binar Academy · Data Science Bootcamp

> REST API untuk analisis sentimen tweet berbahasa Indonesia menggunakan dua model Machine Learning: **LSTM** (Deep Learning) dan **MLP** (Machine Learning klasik), dengan pipeline text cleansing dan kamus kata alay.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-UI-85EA2D?style=flat&logo=swagger&logoColor=black)

---

## 👥 Tim

| Nama | Role |
|------|------|
| Riyadi Nugroho | Data Scientist |
| Khoirul Anam | Data Scientist |
| Ursula Andrea | Data Scientist |

---

## 📌 Tentang Project

Project **Platinum Challenge** dari Binar Academy ini membangun REST API sentiment analysis untuk tweet berbahasa Indonesia. API ini mampu mengklasifikasikan teks ke dalam tiga kelas sentimen: **Positive**, **Neutral**, dan **Negative** menggunakan dua pendekatan berbeda.

---

## ✨ Fitur

- 🧹 **Text Cleansing Pipeline** — Normalisasi teks: hapus USER/RT/URL, lowercase, hapus emoji, ganti kata alay
- 📖 **Kamus Alay** — 15.167 entri normalisasi kata tidak baku → baku
- 🧠 **Model LSTM** — Deep learning berbasis sequence untuk prediksi sentimen
- 🤖 **Model MLP** — Multi-Layer Perceptron dengan TF-IDF untuk prediksi sentimen
- 📄 **Input Teks** — Prediksi sentimen dari input teks langsung
- 📁 **Input File CSV** — Prediksi sentimen secara batch dari file CSV tweet
- 🗃️ **SQLite Database** — Penyimpanan kamus alay saat runtime
- 📚 **Swagger UI** — Dokumentasi dan testing API interaktif

---

## 📊 Dataset

### 1. File_Tweet.csv — Dataset Tweet Berlabel
**13.169 tweet** dengan label hate speech:

| Kolom | Deskripsi |
|-------|-----------|
| `Tweet` | Isi tweet |
| `HS` | Hate Speech (0/1) |
| `Abusive` | Konten abusif (0/1) |
| `HS_*` | Sub-kategori hate speech (Individual, Group, Religion, Race, Physical, Gender, Other) |
| `HS_Weak/Moderate/Strong` | Intensitas hate speech |

### 2. train_preprocess.tsv.txt — Data Training Sentimen
**11.000 tweet** yang sudah dipreprocess dengan label sentimen 3 kelas:
- `positive` — sentimen positif
- `neutral` — sentimen netral
- `negative` — sentimen negatif

### 3. new_kamusalay.csv — Kamus Kata Alay
**15.167 entri** pasangan kata tidak baku → kata baku (contoh: `gw` → `saya`, `yg` → `yang`)

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|----------|-----------|
| Web Framework | Flask |
| API Docs | Flasgger (Swagger UI) |
| Deep Learning | TensorFlow / Keras (LSTM) |
| Machine Learning | Scikit-learn (MLP + TF-IDF) |
| NLP | NLTK (tokenisasi) |
| Database | SQLite 3 |
| Data Processing | Pandas |

---

## 📡 API Endpoints

| Method | Endpoint | Deskripsi | Model |
|--------|----------|-----------|-------|
| `GET` | `/` | Info tim dan project | — |
| `POST` | `/text_sentiment_LSTM` | Prediksi sentimen dari teks | LSTM |
| `POST` | `/text_sentiment_MLP` | Prediksi sentimen dari teks | MLP |
| `POST` | `/Tweet_Sentiment_LSTM` | Prediksi sentimen dari file CSV | LSTM |
| `POST` | `/Tweet_Sentiment_MLP` | Prediksi sentimen dari file CSV | MLP |

### Contoh Request — Text Input

```bash
curl -X POST http://localhost:5000/text_sentiment_MLP \
  -F "text=Pelayanannya bagus banget, saya puas!"
```

### Contoh Response

```json
{
  "Description": "Text Sentiment Analysis",
  "Input_Text": "Pelayanannya bagus banget, saya puas!",
  "Sentiment": "Positive"
}
```

### Contoh Request — File CSV

File CSV harus memiliki kolom `Tweet`. Contoh isi:
```
Tweet
"Produk ini sangat memuaskan"
"Pengiriman lama banget kecewa"
```

---

## 🚀 Cara Instalasi & Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/[USERNAME]/Data_Science_Challenge-Platinum.git
cd Data_Science_Challenge-Platinum
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

### 4. Download NLTK data

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
```

### 5. Siapkan model files

> ⚠️ File model tidak di-include di repo karena ukurannya besar. Letakkan file berikut sebelum menjalankan API:
>
> - `Model_LSTM/model_LSTM.h5` — trained LSTM model
> - `Model_LSTM/text_preprocessing.pickle` — tokenizer
> - `Model_MLP/model_MLP.pickle` — trained MLP model

Latih ulang model menggunakan notebook:
- `Model_LSTM/LSTM_Sentiment.ipynb`
- `Model_MLP/MLP_Sentiment.ipynb`

### 6. Jalankan API

```bash
python API.py
```

API berjalan di: `http://localhost:5000`
Swagger UI: `http://localhost:5000/docs/`

---

## 📁 Struktur Project

```
Platinum-Challenge-Binar-Academy/
├── Dataset/
│   ├── File_Tweet.csv              # Dataset tweet berlabel (13.169 baris)
│   ├── new_kamusalay.csv           # Kamus alay (15.167 entri)
│   └── train_preprocess.tsv.txt   # Data training sentimen (11.000 baris)
├── EDA & Report Analysis/
│   ├── EDA-PLATINUM-CHALLENGE.ipynb    # Notebook exploratory data analysis
│   └── Report Sentiment Analysis.pptx # Laporan presentasi
├── Kalkulasi Neural Network/
│   └── Kalkulasi Neural Network.pdf   # Dokumentasi arsitektur NN
├── Model_LSTM/
│   ├── LSTM_Sentiment.ipynb           # Notebook training LSTM
│   ├── model_LSTM.h5                  # ⚠️ Generate via notebook (tidak di-repo)
│   └── text_preprocessing.pickle      # Tokenizer
├── Model_MLP/
│   ├── MLP_Sentiment.ipynb            # Notebook training MLP
│   └── model_MLP.pickle               # Trained MLP model
├── docs/
│   ├── team.yml
│   ├── text_LSTM.yml
│   ├── text_MLP.yml
│   ├── file_LSTM.yml
│   └── file_MLP.yml
├── API.py                             # Flask app utama
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📓 Notebook & Analisis

| File | Deskripsi |
|------|-----------|
| `EDA & Report Analysis/EDA-PLATINUM-CHALLENGE.ipynb` | Exploratory Data Analysis dataset |
| `Model_LSTM/LSTM_Sentiment.ipynb` | Training & evaluasi model LSTM |
| `Model_MLP/MLP_Sentiment.ipynb` | Training & evaluasi model MLP |
| `Kalkulasi Neural Network/Kalkulasi Neural Network.pdf` | Dokumentasi arsitektur dan perhitungan NN |

---

## 📄 Lisensi

Project ini dibuat untuk keperluan edukasi dalam program **Binar Academy Data Science Bootcamp**.

---

<p align="center">Dibuat dengan 🐍 Python · TensorFlow · Flask · Binar Academy Platinum Challenge</p>
