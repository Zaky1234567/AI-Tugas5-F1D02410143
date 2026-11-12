# Tugas 5 AI - Membuat Sistem Pakar Sederhana

**1. Identitas**
* Nama: Zaky
* NIM: F1D02410143
* Kelas: C

**2. Topik dan Cara Menjalankan Program**
* Topik: Diagnosis Gangguan Koneksi Internet dan WiFi
* Bahasa: Python 3
* Cara menjalankan: Buka terminal/command prompt di direktori file, lalu ketikkan perintah `python main.py`

**3. Daftar Sumber dan Tabel Aturan**
* **S1**: "Memperbaiki masalah koneksi Wi-Fi di Windows", Penerbit: Microsoft. URL: https://support.microsoft.com/id-id/windows/memperbaiki-masalah-koneksi-wi-fi-di-windows-9424a1f7-6a3b-65a6-4d78-7f07eee84d2c (diakses 12 November 2026).
* **S2**: "Arti Lampu Indikator Wi-Fi IndiHome yang Berkedip", Penerbit: Telkomsel. URL: https://www.telkomsel.com/jelajah/jelajah-lifestyle/arti-lampu-indikator-wi-fi-indihome-yang-berkedip-ih (diakses 12 November 2026).


**4. Metode yang Dipilih**
Saya menggunakan **Forward Chaining (FC)**. Alasannya karena program ini dirancang untuk melakukan diagnosis (troubleshooting) jaringan, yang mana alur pikirnya bergerak dari mengumpulkan fakta/gejala awal dari pengguna untuk merunut maju hingga mencapai sebuah kesimpulan akhir.

**5. Tiga Kasus Uji**
Berikut adalah screenshot pengujian program:

**Kasus 1: Masalah Catu Daya**
![Kasus 1] (screenshot/kasus1.png)

**Kasus 2: Gangguan Fisik Kabel Optik**
![Kasus 2] (screenshot/kasus2.png)

**Kasus 3: Kasus Negatif (Tidak Ada Kesimpulan)**
![Kasus 3] (screenshot/kasus3.png)

**6. Batas Keberlakuan**
Aturan berasal dari dokumentasi umum troubleshooting jaringan (Microsoft dan Telkomsel) dan hanya mencakup masalah daya, fisik fiber optik, dan jangkauan sinyal. Hasilnya berupa saran awal untuk pengguna rumahan, bukan keputusan teknis akhir untuk level enterprise.

**7. Penggunaan Alat Bantu AI**
Saya menggunakan AI (Gemini) sebagai mitra diskusi untuk merancang struktur aturan (JSON) dan memahami alur algoritma metode Forward Chaining. Namun, kode program dipelajari, dieksekusi, dan dimengerti secara mandiri.