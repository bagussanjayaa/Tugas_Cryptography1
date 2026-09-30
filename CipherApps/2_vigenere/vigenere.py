def enkripsi(pesan, kunci):
    hasil = ""
    indeks_kunci = 0

    kunci = kunci.upper()

    for karakter in pesan:
        if karakter.isalpha():
            dasar = ord('A') if karakter.isupper() else ord('a')

            p = ord(karakter.upper()) - ord('A')
            k = ord(kunci[indeks_kunci % len(kunci)]) - ord('A')

            nilai = (p + k) % 26

            hasil += chr(nilai + dasar)

            indeks_kunci += 1
        else:
            hasil += karakter

    return hasil


def dekripsi(pesan, kunci):
    hasil = ""
    indeks_kunci = 0

    kunci = kunci.upper()

    for karakter in pesan:
        if karakter.isalpha():
            dasar = ord('A') if karakter.isupper() else ord('a')

            c = ord(karakter.upper()) - ord('A')
            k = ord(kunci[indeks_kunci % len(kunci)]) - ord('A')

            nilai = (c - k) % 26

            hasil += chr(nilai + dasar)

            indeks_kunci += 1
        else:
            hasil += karakter

    return hasil


def validasi_kunci(kunci):
    return kunci.isalpha() and len(kunci) > 0


def tampilkan_menu():
    print("\n======================================")
    print("         VIGENERE CIPHER")
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
            print("Kunci hanya boleh berisi huruf.")
            continue

        hasil = enkripsi(pesan, kunci)

        print("\nHasil enkripsi :", hasil)

    elif pilihan == "2":
        pesan = input("Masukkan ciphertext : ")
        kunci = input("Masukkan kata kunci : ")

        if not validasi_kunci(kunci):
            print("Kunci hanya boleh berisi huruf.")
            continue

        hasil = dekripsi(pesan, kunci)

        print("\nHasil dekripsi :", hasil)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")