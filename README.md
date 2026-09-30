# Tugas_Cryptography1

# Bagus Sanjaya

# Kriptograpi

# I241E

# Sistem Cipher Klasik

Repository ini berisi **3 aplikasi sistem cipher klasik** yang dibuat menggunakan bahasa pemrograman **Python**. Aplikasi ini dibuat untuk memahami konsep dasar kriptografi klasik, khususnya proses **enkripsi dan dekripsi**.

Tiga metode cipher yang digunakan adalah:

1. **Caesar Cipher**
2. **Vigenère Cipher**
3. **Columnar Transposition Cipher**

Ketiga metode tersebut dipilih karena mewakili dua teknik dasar dalam kriptografi klasik, yaitu **substitusi** dan **transposisi**. Pada materi, cipher klasik dijelaskan sebagai sistem yang memproses pesan berupa huruf alfabet dan termasuk ke dalam kriptografi kunci-simetri.

---

## Tujuan

Tujuan dari pembuatan aplikasi ini adalah:

* Memahami konsep dasar kriptografi klasik.
* Memahami proses enkripsi dan dekripsi.
* Menerapkan algoritma Caesar Cipher.
* Menerapkan algoritma Vigenère Cipher.
* Menerapkan algoritma Columnar Transposition Cipher.
* Memahami perbedaan teknik substitusi dan transposisi.
* Mengimplementasikan konsep cipher klasik ke dalam program Python.

---

# Dasar Teori

Kriptografi klasik mempunyai dua teknik dasar, yaitu:

### 1. Substitusi

Teknik substitusi dilakukan dengan cara **mengganti huruf plaintext dengan huruf ciphertext**.

Contohnya:

```text
Plaintext  : MENGANTUK
Ciphertext : ...
```

### 2. Transposisi

Teknik transposisi tidak mengganti huruf, tetapi **mengubah posisi atau susunan huruf** pada plaintext.

Contohnya:

```text
Plaintext  : MENGANTUK
Ciphertext : ...
```

Materi menjelaskan bahwa cipher substitusi menggunakan teknik penggantian huruf, sedangkan cipher transposisi menggunakan perubahan posisi huruf. Kombinasi keduanya disebut **product cipher atau super-enkripsi**.

---

# 1. Caesar Cipher

## Pengertian

Caesar Cipher merupakan salah satu contoh **cipher substitusi**. Setiap huruf plaintext digeser beberapa posisi berdasarkan nilai kunci.

Misalnya kunci yang digunakan adalah `3`:

```text
A → D
B → E
C → F
D → G
...
X → A
Y → B
Z → C
```

Pada materi, Caesar Cipher menggunakan pergeseran tiga huruf ke kanan sebagai contoh.

## Rumus

### Enkripsi

```text
C = (P + K) mod 26
```

### Dekripsi

```text
P = (C - K) mod 26
```

Keterangan:

```text
P = Plaintext
C = Ciphertext
K = Kunci
```

Rumus tersebut digunakan untuk melakukan pergeseran huruf pada alfabet.

## Contoh

Plaintext:

```text
SISTEM INFORMASI
```

Kunci:

```text
3
```

Hasil enkripsi:

```text
VLVWHP LQIRUPDVL
```

Kemudian ciphertext tersebut didekripsi menggunakan kunci yang sama:

```text
VLVWHP LQIRUPDVL
```

Hasil:

```text
SISTEM INFORMASI
```

---

# 2. Vigenère Cipher

## Pengertian

Vigenère Cipher termasuk ke dalam **cipher abjad-majemuk (polyalphabetic substitution cipher)**.

Berbeda dengan Caesar Cipher yang menggunakan satu nilai pergeseran untuk seluruh pesan, Vigenère menggunakan **kata kunci** yang dapat menghasilkan pergeseran berbeda pada setiap huruf.

Materi menjelaskan bahwa cipher abjad-majemuk dibuat dari sejumlah cipher abjad-tunggal dengan kunci yang berbeda.

## Contoh Kunci

Misalnya:

```text
Plaintext : SISTEM INFORMASI
Kunci     : KUNCI
```

Kunci akan diulang mengikuti panjang plaintext:

```text
Plaintext : S I S T E M I N F O R M A S I
Kunci     : K U N C I K U N C I K U N C I
```

Setiap huruf plaintext kemudian diproses menggunakan huruf kunci yang sesuai.

Konsep pengulangan kunci seperti ini juga ditunjukkan dalam contoh Vigenère pada materi.

## Contoh

Input:

```text
Plaintext : SISTEM INFORMASI
Kunci     : KUNCI
```

Output ciphertext:

```text
COFVM WEAHWBGNUQ
```

Ketika ciphertext didekripsi menggunakan kunci:

```text
KUNCI
```

maka plaintext kembali menjadi:

```text
SISTEM INFORMASI
```

---

# 3. Columnar Transposition Cipher

## Pengertian

Columnar Transposition Cipher merupakan salah satu **cipher transposisi**.

Pada metode ini, huruf plaintext tidak diganti. Huruf hanya disusun kembali berdasarkan posisi atau urutan kolom.

Materi menjelaskan bahwa cipher transposisi dilakukan dengan mengubah posisi huruf dalam plaintext. Contoh cipher transposisi yang diberikan adalah **Columnar Transposition Cipher** dan **Rail Fence Transposition Cipher**.

## Proses Enkripsi

Misalnya:

```text
Plaintext : SISTEM DAN TEKNOLOGI
Kunci     : TOMBAK
```

Spasi dihilangkan:

```text
SISTEMDANTEKNOLOGI
```

Kemudian plaintext disusun ke dalam tabel berdasarkan panjang kunci:

```text
T O M B A K
------------
S I S T E M
D A N T E K
N O L O G I
```

Urutan huruf pada kata `TOMBAK` digunakan untuk menentukan urutan kolom yang dibaca.

Pada materi, kata kunci `TOMBAK` juga digunakan sebagai contoh dan pembacaan ciphertext dilakukan secara vertikal sesuai urutan huruf dalam kata kunci.

## Dekripsi

Pada proses dekripsi, ciphertext dimasukkan kembali ke kolom sesuai urutan kunci, kemudian dibaca secara horizontal untuk mendapatkan plaintext.

Hasil akhirnya:

```text
SISTEMDANTEKNOLOGI
```

---

# Teknologi yang Digunakan

| Teknologi      | Keterangan           |
| -------------- | -------------------- |
| Python         | Bahasa pemrograman   |
| CMD / Terminal | Menjalankan aplikasi |
| Git            | Version control      |
| GitHub         | Repository project   |

Project ini tidak membutuhkan database atau library tambahan.

---

# Struktur Folder

```text
CipherApps/
│
├── 1_caesar/
│   └── caesar.py
│
├── 2_vigenere/
│   └── vigenere.py
│
└── 3_columnar/
    └── columnar.py
```

Keterangan:

```text
1_caesar/
```

Berisi program Caesar Cipher.

```text
2_vigenere/
```

Berisi program Vigenère Cipher.

```text
3_columnar/
```

Berisi program Columnar Transposition Cipher.

---

# Instalasi dan Menjalankan Program

## 1. Install Python

Pastikan Python sudah terinstall.

Cek menggunakan CMD:

```bash
python --version
```

Contoh:

```text
Python 3.12.10
```

---

## 2. Clone Repository

Clone repository menggunakan:

```bash
git clone https://github.com/USERNAME/CipherApps.git
```

Masuk ke folder:

```bash
cd CipherApps
```

---

# Menjalankan Caesar Cipher

Masuk ke folder:

```bash
cd 1_caesar
```

Jalankan:

```bash
python caesar.py
```

Tampilan menu:

```text
======================================
          CAESAR CIPHER
======================================
1. Enkripsi
2. Dekripsi
3. Keluar
======================================
```

---

# Menjalankan Vigenère Cipher

Kembali ke folder utama:

```bash
cd ..
```

Masuk:

```bash
cd 2_vigenere
```

Jalankan:

```bash
python vigenere.py
```

Tampilan:

```text
======================================
         VIGENERE CIPHER
======================================
1. Enkripsi
2. Dekripsi
3. Keluar
======================================
```

---

# Menjalankan Columnar Transposition

Kembali:

```bash
cd ..
```

Masuk:

```bash
cd 3_columnar
```

Jalankan:

```bash
python columnar.py
```

Tampilan:

```text
======================================
    COLUMNAR TRANSPOSITION CIPHER
======================================
1. Enkripsi
2. Dekripsi
3. Keluar
======================================
```

---

# Pengujian Program

## Pengujian Caesar Cipher

### Enkripsi

```text
Plaintext : HALO DUNIA
Kunci     : 3
```

Proses:

```text
H → K
A → D
L → O
O → R
```

Hasil ciphertext:

```text
K D O R G X Q L D
```

### Dekripsi

Ciphertext:

```text
K D O R G X Q L D
```

Kunci:

```text
3
```

Hasil:

```text
HALO DUNIA
```

---

## Pengujian Vigenère Cipher

### Enkripsi

```text
Plaintext : SISTEM INFORMASI
Kunci     : KUNCI
```

Kunci diulang:

```text
S I S T E M I N F O R M A S I
K U N C I K U N C I K U N C I
```

Hasil:

```text
COFVM WEAHWBGNUQ
```

### Dekripsi

```text
Ciphertext : COFVM WEAHWBGNUQ
Kunci      : KUNCI
```

Hasil:

```text
SISTEM INFORMASI
```

---

## Pengujian Columnar Transposition

### Enkripsi

```text
Plaintext : SISTEM DAN TEKNOLOGI
Kunci     : TOMBAK
```

Plaintext tanpa spasi:

```text
SISTEMDANTEKNOLOGI
```

Kemudian disusun menjadi tabel:

```text
T O M B A K
-----------
S I S T E M
D A N T E K
N O L O G I
```

Kolom kemudian dibaca berdasarkan urutan alfabet dari kata kunci.

### Dekripsi

Ciphertext dimasukkan kembali dengan kunci:

```text
TOMBAK
```

Hasil:

```text
SISTEMDANTEKNOLOGI
```

---

# Perbandingan Ketiga Cipher

| Aspek           | Caesar           | Vigenère                     | Columnar           |
| --------------- | ---------------- | ---------------------------- | ------------------ |
| Teknik          | Substitusi       | Substitusi                   | Transposisi        |
| Jenis           | Monoalphabetic   | Polyalphabetic               | Transposition      |
| Kunci           | Angka            | Kata                         | Kata               |
| Contoh kunci    | `3`              | `KUNCI`                      | `TOMBAK`           |
| Mengubah huruf  | Ya               | Ya                           | Tidak              |
| Mengubah posisi | Tidak            | Tidak                        | Ya                 |
| Enkripsi        | Pergeseran       | Pergeseran berdasarkan kunci | Penyusunan kolom   |
| Dekripsi        | Pergeseran balik | Pergeseran balik             | Penyusunan kembali |

---

# 📝 Analisis

Dari ketiga aplikasi yang dibuat, terdapat perbedaan pada proses enkripsinya.

**Caesar Cipher** merupakan metode yang paling sederhana karena setiap huruf hanya digeser berdasarkan satu nilai kunci. Materi juga menjelaskan bahwa Caesar Cipher memiliki jumlah kunci yang sedikit, yaitu 26 kunci, sehingga dapat dicoba menggunakan exhaustive key search atau brute force.

**Vigenère Cipher** menggunakan beberapa pergeseran berdasarkan kata kunci. Karena kunci dapat berbeda untuk setiap posisi huruf, metode ini termasuk cipher abjad-majemuk.

Sedangkan **Columnar Transposition Cipher** bekerja dengan cara mengubah posisi karakter. Jadi huruf pada plaintext tetap sama, tetapi susunannya berubah menjadi ciphertext.

Ketiga metode tersebut menunjukkan bahwa proses pengamanan pesan dapat dilakukan dengan cara yang berbeda, baik dengan mengganti karakter maupun dengan mengubah susunan karakter.

---

# Kelebihan dan Kekurangan

## Caesar Cipher

### Kelebihan

* Algoritmanya sederhana.
* Mudah dipahami dan dibuat.
* Proses enkripsi dan dekripsi cepat.
* Cocok untuk memahami dasar substitusi.

### Kekurangan

* Jumlah kunci sedikit.
* Mudah dicoba menggunakan brute force.
* Tidak cocok digunakan sebagai sistem keamanan modern.

Materi juga menjelaskan bahwa Caesar mudah dipecahkan karena hanya memiliki 26 kemungkinan kunci.

---

## Vigenère Cipher

### Kelebihan

* Menggunakan kata kunci.
* Pergeseran huruf tidak selalu sama.
* Lebih kompleks dibanding Caesar Cipher.

### Kekurangan

* Tetap merupakan cipher klasik.
* Penggunaan kunci yang pendek atau berulang dapat menjadi kelemahan dalam analisis tertentu.
* Tidak ditujukan untuk menggantikan algoritma kriptografi modern.

---

## Columnar Transposition Cipher

### Kelebihan

* Tidak langsung mengganti karakter plaintext.
* Susunan ciphertext menjadi berbeda dari plaintext.
* Konsepnya cukup mudah diterapkan.

### Kekurangan

* Posisi huruf masih berasal dari plaintext.
* Jika sistem dan kunci diketahui, pesan dapat dikembalikan.
* Termasuk kriptografi klasik sehingga tidak digunakan sebagai pengamanan modern.

---

# Kesimpulan

Dari pembuatan tiga aplikasi sistem cipher, yaitu **Caesar Cipher, Vigenère Cipher, dan Columnar Transposition Cipher**, dapat dipahami bahwa kriptografi klasik mempunyai beberapa cara untuk mengamankan sebuah pesan.

Caesar Cipher menggunakan teknik substitusi dengan melakukan pergeseran huruf berdasarkan kunci. Vigenère Cipher menggunakan teknik substitusi abjad-majemuk dengan kata kunci yang digunakan berulang sesuai panjang pesan. Sedangkan Columnar Transposition Cipher menggunakan teknik transposisi dengan mengubah posisi atau susunan huruf tanpa mengganti karakter aslinya.

Melalui pembuatan ketiga aplikasi ini, konsep dasar **enkripsi, dekripsi, plaintext, ciphertext, kunci, substitusi, dan transposisi** dapat dipahami sekaligus diterapkan ke dalam program Python.

---

# Referensi

1. R. Munir, **“Ragam Cipher Klasik (Bagian 1)”**, Bahan Kuliah IF4020 Kriptografi, Program Studi Teknik Informatika, Sekolah Teknik Elektro dan Informatika, Institut Teknologi Bandung, 2025.

2. Materi perkuliahan mengenai **Caesar Cipher, Cipher Abjad-Majemuk, dan Cipher Transposisi** yang digunakan sebagai dasar pembuatan aplikasi ini.

---

## Author

**Bagus Sanjaya**

Project ini dibuat untuk keperluan pembelajaran dan tugas perkuliahan **Kriptografi**.
