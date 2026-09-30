def buat_urutan_kolom(kunci):
    # Mengurutkan pasangan huruf dan posisi asli
    pasangan = []

    for i, huruf in enumerate(kunci.upper()):
        pasangan.append((huruf, i))

    pasangan.sort()

    urutan = []

    for nomor, (_, posisi) in enumerate(pasangan):
        urutan.append((nomor + 1, posisi))

    return urutan


def enkripsi(plaintext, kunci):
    kunci = kunci.upper()
    plaintext = plaintext.replace(" ", "").upper()

    jumlah_kolom = len(kunci)

    # Tambahkan X jika jumlah karakter tidak memenuhi tabel
    while len(plaintext) % jumlah_kolom != 0:
        plaintext += "X"

    jumlah_baris = len(plaintext) // jumlah_kolom

    tabel = []

    posisi = 0

    for i in range(jumlah_baris):
        baris = []

        for j in range(jumlah_kolom):
            baris.append(plaintext[posisi])
            posisi += 1

        tabel.append(baris)

    urutan = buat_urutan_kolom(kunci)

    ciphertext = ""

    for _, kolom in urutan:
        for baris in tabel:
            ciphertext += baris[kolom]

    return ciphertext


def dekripsi(ciphertext, kunci):
    kunci = kunci.upper()
    ciphertext = ciphertext.replace(" ", "").upper()

    jumlah_kolom = len(kunci)
    jumlah_baris = len(ciphertext) // jumlah_kolom

    tabel = [
        [""] * jumlah_kolom
        for _ in range(jumlah_baris)
    ]

    urutan = buat_urutan_kolom(kunci)

    posisi = 0

    for _, kolom in urutan:
        for baris in range(jumlah_baris):
            tabel[baris][kolom] = ciphertext[posisi]
            posisi += 1

    plaintext = ""

    for baris in tabel:
        plaintext += "".join(baris)

    # Hilangkan X padding di bagian akhir
    plaintext = plaintext.rstrip("X")

    return plaintext


def validasi_kunci(kunci):
    kunci = kunci.upper()

    if not kunci.isalpha():
        return False

    if len(set(kunci)) != len(kunci):
        return False

    return len(kunci) > 0


def tampilkan_menu():
    print("\n======================================")
    print("    COLUMNAR TRANSPOSITION CIPHER")
    print("======================================")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    print("======================================")


while True:
    tampilkan_menu()

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        pesan = input("Masukkan plaintext : ")
        kunci = input("Masukkan kata kunci : ")

        if not validasi_kunci(kunci):
            print("Kunci harus berupa huruf dan tidak boleh ada huruf yang sama.")
            continue

        hasil = enkripsi(pesan, kunci)

        print("\nHasil enkripsi :", hasil)

    elif pilihan == "2":
        pesan = input("Masukkan ciphertext : ")
        kunci = input("Masukkan kata kunci : ")

        if not validasi_kunci(kunci):
            print("Kunci harus berupa huruf dan tidak boleh ada huruf yang sama.")
            continue

        if len(pesan.replace(" ", "")) % len(kunci) != 0:
            print("Panjang ciphertext tidak sesuai dengan panjang kunci.")
            continue

        hasil = dekripsi(pesan, kunci)

        print("\nHasil dekripsi :", hasil)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")