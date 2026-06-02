### Nama: 
Ilan Hawwari Prasojo

### NRP
5024241039

# Aplikasi Chat Room Berbasis TCP Socket
Proyek ini adalah implementasi sistem chat room (ruang obrolan) berbasis Command Line Interface (CLI) menggunakan arsitektur Client-Server. Aplikasi ini berjalan di atas protokol TCP (Transmission Control Protocol) menggunakan pustaka standar Python. Sistem mendukung komunikasi banyak pengguna (multi-client) secara serentak dan real-time dengan memanfaatkan multi-threading.

# Fitur
Komunikasi Jaringan TCP: Menjamin pengiriman pesan yang andal (reliable) antar pengguna.

Arsitektur Multi-Threading: Memisahkan proses input pengguna dan penerimaan data dari server sehingga tidak terjadi blocking I/O.

Sistem Broadcasting: Server secara otomatis mendistribusikan pesan dari satu klien ke seluruh klien lain yang terhubung.

Manajemen Sesi: Pemberitahuan otomatis ketika pengguna baru bergabung ke dalam chat room dan penanganan otomatis saat klien memutus koneksi.

@ Persyaratan Sistem
Aplikasi ini hanya menggunakan library bawaan Python, sehingga tidak memerlukan instalasi package pihak ketiga.

Python 3.x terinstal pada sistem.

Modul standar yang digunakan: socket, threading, sys.

# Struktur File
```
server.py : Berisi kode untuk menginisialisasi server, menerima koneksi, dan mengelola rute pesan (broadcasting).

client.py : Berisi antarmuka pengguna untuk menghubungkan ke server, mengirim, dan menerima pesan.
```
# Panduan Penggunaan
1. Menjalankan Server
Server harus dijalankan terlebih dahulu untuk membuka port jaringan dan mendengarkan koneksi masuk.
Buka terminal/command prompt dan jalankan perintah berikut:

Bash
python server.py
Catatan: Server secara default akan berjalan pada HOST = 0.0.0.0 dan PORT = 10005.

2. Menjalankan Klien
Buka jendela terminal baru untuk setiap pengguna yang ingin bergabung ke dalam chat room. Pastikan jendela terminal server tetap berjalan.
Jalankan perintah berikut pada terminal baru:

Bash
python client.py
Catatan: Klien secara default dikonfigurasi untuk terhubung ke SERVER_IP = 127.0.0.1 (localhost). Jika menjalankan klien dari komputer yang berbeda dalam satu jaringan, ubah variabel SERVER_IP di client.py menjadi alamat IP komputer server.

3. Instruksi Obrolan
Mengirim Pesan: Ketik pesan pada terminal klien dan tekan Enter untuk mengirim.

Keluar dari Chat Room: Ketik exit (tidak peka huruf besar/kecil) dan tekan Enter untuk memutus koneksi dengan aman dan menutup program.

#Detail Teknis Arsitektur
Konkurensi Server: Setiap kali klien baru melakukan koneksi, server menggunakan metode accept() untuk membuat objek socket baru dan mengalokasikannya ke thread terpisah untuk dipantau secara mandiri.

Isolasi I/O Klien: Klien mengeksekusi dua alur (threads) utama:

Main Thread: Menangani pembacaan fungsi input() dari keyboard dan transmisi data.

Daemon Thread: Melakukan iterasi fungsi recv() untuk menampilkan pesan yang diterima dari server ke layar stdout tanpa mengganggu proses pengetikan.
