# **Sentiment Analysis Google Playstore**

## **Deskripsi Proyek**
Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan aplikasi di Google Playstore. Analisis ini menggunakan teknik Natural Language Processing (NLP) untuk mengkategorikan ulasan pengguna menjadi sentimen positif dan negatif. Hasil dari proyek ini dapat digunakan untuk memahami pengalaman pengguna dengan aplikasi, dan memberikan wawasan bagi pengembang aplikasi untuk perbaikan.

## **Fitur Utama**
- **Scraping ulasan** dari Google Playstore menggunakan library `scrap_reviews`.
- Mengkategorikan ulasan aplikasi sebagai **positif** atau **negatif**.
- Menggunakan **WordCloud** untuk visualisasi kata-kata yang sering muncul dalam ulasan.
- Analisis berdasarkan aspek-aspek seperti **bug**, **kinerja aplikasi**, dan **fitur baru**.
- Menggunakan model **lexicon-based** untuk analisis sentimen.

## **Hasil**
Proyek ini menghasilkan:

- Scraping ulasan dari Google Playstore secara otomatis.
- Klasifikasi ulasan berdasarkan sentimen.
- WordCloud untuk ulasan positif dan negatif.
- Insight mengenai keluhan utama pengguna dan aspek yang mereka sukai dari aplikasi.

## **Struktur Kategori**

- [data/](./data)               - Folder untuk dataset ulasan Google Playstore
- [notebooks/](./notebooks)     - Jupyter notebooks untuk analisis
- [src/](./src)                 - Source code untuk preprocessing dan scrapping data
- [README.md](./README.md)      - Penjelasan proyek ini

## Teknologi yang Digunakan
- Python
- Pandas
- NLTK
- Scikit-learn
- Matplotlib
- WordCloud
- scrap_reviews
