def enkripsi(pesan, kunci):
    hasil = ""

    for karakter in pesan:
        if karakter.isalpha():
            dasar = ord('A') if karakter.isupper() else ord('a')

            nilai = (ord(karakter) - dasar + kunci) % 26
            hasil += chr(nilai + dasar)
        else:
            hasil += karakter

    return hasil


def dekripsi(pesan, kunci):
    hasil = ""

    for karakter in pesan:
        if karakter.isalpha():
            dasar = ord('A') if karakter.isupper() else ord('a')

            nilai = (ord(karakter) - dasar - kunci) % 26
            hasil += chr(nilai + dasar)
        else:
            hasil += karakter

    return hasil


def tampilkan_menu():
    print("\n======================================")
    print("          CAESAR CIPHER")
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

        try:
            kunci = int(input("Masukkan kunci (0-25) : "))

            if kunci < 0 or kunci > 25:
                print("Kunci harus berada antara 0 sampai 25.")
                continue

            hasil = enkripsi(pesan, kunci)

            print("\nHasil enkripsi :", hasil)

        except ValueError:
            print("Kunci harus berupa angka.")

    elif pilihan == "2":
        pesan = input("Masukkan ciphertext : ")

        try:
            kunci = int(input("Masukkan kunci (0-25) : "))

            if kunci < 0 or kunci > 25:
                print("Kunci harus berada antara 0 sampai 25.")
                continue

            hasil = dekripsi(pesan, kunci)

            print("\nHasil dekripsi :", hasil)

        except ValueError:
            print("Kunci harus berupa angka.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")