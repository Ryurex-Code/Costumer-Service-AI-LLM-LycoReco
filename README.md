# Café LycoReco - Layanan Pelanggan Berbasis AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Latar Belakang dan Referensi Nama

Proyek ini terinspirasi dari anime populer "Lycoris Recoil". Nama "Café LycoReco" diambil dari nama kafe tempat para karakter utama bekerja dan berinteraksi. Layaknya kafe tersebut yang menawarkan berbagai layanan, proyek ini bertujuan untuk menyediakan layanan pelanggan yang interaktif dan informatif melalui chatbot berbasis kecerdasan buatan.

## Teknologi yang Digunakan

Proyek ini dibangun menggunakan teknologi berikut:

* **Gradio:** Sebuah *framework* Python yang memungkinkan pembuatan antarmuka pengguna berbasis web untuk model *machine learning* dengan cepat.
* **Groq:** Sebuah platform yang menyediakan akses ke model bahasa besar (LLM) berperforma tinggi, dalam proyek ini menggunakan model `llama3-8b-8192`.
* **Python:** Bahasa pemrograman utama yang digunakan dalam pengembangan.
* **dotenv:** Pustaka Python untuk memuat variabel lingkungan dari file `.env`.

## Cara Penggunaan

Berikut adalah langkah-langkah untuk menjalankan aplikasi layanan pelanggan ini:

1.  **Prasyarat:**
    * Pastikan Anda telah menginstal **Python** di sistem Anda.
    * Instal `pip` (Python package installer) jika belum terpasang.

2.  **Kloning Repositori (opsional):**
    Jika kode ini berada di repositori GitHub, Anda dapat mengkloningnya menggunakan perintah:
    ```bash
    git clone <URL_repositori>
    cd <nama_repositori>
    ```

3.  **Instal Dependensi:**
    Pastikan Anda telah menginstal semua pustaka yang diperlukan. Anda dapat melakukannya dengan menjalankan perintah berikut di terminal atau command prompt:
    ```bash
    pip install gradio groq python-dotenv
    ```

4.  **Konfigurasi API Key:**
    * Buat sebuah file bernama `.env` di direktori proyek Anda.
    * Tambahkan API key dari Groq ke dalam file `.env` dengan format berikut:
        ```
        GROQ_API_KEY=YOUR_GROQ_API_KEY_DI_SINI
        ```
        Pastikan untuk mengganti `YOUR_GROQ_API_KEY_DI_SINI` dengan API key Groq Anda yang sebenarnya.

5.  **Konfigurasi Prompt Sistem (opsional):**
    * Pastikan Anda memiliki file bernama `prompt.txt` di direktori proyek Anda.
    * File ini berisi prompt sistem yang akan digunakan untuk mengarahkan perilaku chatbot. Anda dapat memodifikasi isi file ini sesuai dengan kebutuhan Anda.

6.  **Menjalankan Aplikasi:**
    Buka terminal atau command prompt, navigasikan ke direktori proyek Anda, dan jalankan perintah berikut:
    ```bash
    python <nama_file_script_python_anda>.py
    ```
    (Ganti `<nama_file_script_python_anda>.py` dengan nama file skrip Python Anda, misalnya `app.py`).

7.  **Mengakses Antarmuka:**
    Setelah aplikasi berhasil dijalankan, Gradio akan menyediakan URL lokal (biasanya dimulai dengan `http://localhost:` diikuti dengan nomor port). Buka URL tersebut di peramban web Anda untuk mengakses antarmuka layanan pelanggan Café LycoReco.

8.  **Berinteraksi dengan Chatbot:**
    Pada antarmuka web, Anda dapat mengetik pesan Anda di kolom yang tersedia dan chatbot akan memberikan respons berdasarkan prompt sistem dan model `llama3-8b-8192` dari Groq.

## Catatan Penting

* Pastikan API key Groq Anda aman dan tidak dibagikan secara publik.
* Prompt sistem dalam file `prompt.txt` memainkan peran penting dalam menentukan bagaimana chatbot merespons. Eksperimen dengan prompt yang berbeda untuk mendapatkan hasil yang optimal.
* Parameter seperti `temperature`, `max_tokens`, dan `top_p` dalam fungsi `chatbot_response` dapat disesuaikan untuk mengontrol kreativitas dan panjang respons chatbot.
* Aplikasi ini berjalan secara lokal di komputer Anda kecuali Anda secara spesifik menyebarkannya ke platform hosting web.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk informasi lebih lanjut.

## Kontribusi

Jika Anda tertarik untuk berkontribusi pada proyek ini, jangan ragu untuk mengirimkan *pull request* atau membuat *issue* di repositori GitHub.

## Penulis

Ryurex-Corporation
