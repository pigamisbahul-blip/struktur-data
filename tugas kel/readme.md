# 🚌 PesonaTour - Sistem Pemesanan Tiket Bus Pariwisata dengan Panduan Suara

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**PesonaTour** adalah aplikasi pemesanan tiket bus pariwisata berbasis **Circular Linked List** yang dilengkapi dengan **panduan suara interaktif** (Text-to-Speech). Aplikasi ini dibangun dengan Streamlit untuk frontend dan implementasi manual Circular Linked List untuk backend, memberikan pengalaman interaktif dalam memilih dan memesan kursi travel.

---

## 📋 Daftar Isi

- [Fitur Utama](#-fitur-utama)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Struktur Proyek](#-struktur-proyek)
- [Instalasi](#-instalasi)
- [Cara Menjalankan](#-cara-menjalankan)
- [Panduan Penggunaan](#-panduan-penggunaan)
- [Implementasi Circular Linked List](#-implementasi-circular-linked-list)
- [Manajemen Suara](#-manajemen-suara)
- [Antarmuka Pengguna](#-antarmuka-pengguna)
- [Contoh Skenario Penggunaan](#-contoh-skenario-penggunaan)
- [Troubleshooting](#-troubleshooting)
- [Pengembangan Lebih Lanjut](#-pengembangan-lebih-lanjut)
- [Lisensi](#-lisensi)
- [Kontak](#-kontak)

---

## ✨ Fitur Utama

### Core Features
| Fitur | Deskripsi | Status |
|-------|------------|--------|
| 🔄 **Circular Linked List** | Struktur data custom untuk navigasi kursi melingkar tanpa batas | ✅ |
| 🎵 **Panduan Suara** | Informasi kursi, konfirmasi booking, dan error handling dengan suara (gTTS) | ✅ |
| 🪑 **Navigasi Kursi** | Geser ke kursi sebelumnya/berikutnya dengan update suara otomatis | ✅ |
| 📝 **Pemesanan Tiket** | Booking kursi dengan nama penumpang (min. 3 karakter) | ✅ |
| ❌ **Pembatalan Tiket** | Batalkan pemesanan kursi yang sudah terisi | ✅ |
| 📊 **Manifes & Statistik** | Tabel lengkap seluruh kursi, okupansi, dan progress bar | ✅ |
| 🔄 **Visualisasi CLL** | Diagram emoji yang menunjukkan status Circular Linked List | ✅ |
| 🎛️ **Kontrol Suara** | Mute/Unmute, test suara, dan tombol play untuk setiap interaksi | ✅ |

### Additional Features
- ✅ Anti-duplikasi suara (cooldown 2 detik)
- ✅ Reset semua kursi dengan satu tombol
- ✅ Tampilan kursi yang sedang aktif (highlight)
- ✅ Informasi posisi kursi (Depan/Kiri, Tengah/Kanan, Belakang/Kiri, dll)
- ✅ Progress bar persentase okupansi bus

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| **Python** | 3.8+ | Bahasa pemrograman utama |
| **Streamlit** | 1.28+ | Framework untuk membangun frontend interaktif |
| **gTTS** | 2.3+ | Google Text-to-Speech untuk generate suara |
| **Pandas** | 1.5+ | Manajemen data untuk manifest tabel |
| **Tempfile** | Built-in | Manajemen file audio sementara |
| **OS** | Built-in | Operasi file system |

---

## 📁 Struktur Proyek
