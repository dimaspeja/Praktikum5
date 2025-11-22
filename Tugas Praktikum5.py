data = {}

def hitung_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\nProgram Input Nilai")
    print("========================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    menu = input("Pilih menu : ").lower()

    if menu == "l":
        print("\nDaftar Nilai")
        print("====================================================================")
        print(f"| {'NO':^2} | {'NAMA':^12} | {'NIM':^12} | {'TUGAS':^5} | {'UTS':^4} | {'UAS':^4} | {'AKHIR':^7} |")
        print("====================================================================")
        if len(data) == 0:
            print("|                     TIDAK ADA DATA                               |")
        else:
            no = 1
            for nim, item in data.items():
                print(f"| {no:^2d} | {nim:^12s} | {item['nama']:^12s} | "
                      f"{item['tugas']:^5d} | {item['uts']:^4d} | {item['uas']:^4d} | "
                      f"{item['akhir']:^7.2f} |")
                no += 1

        print("====================================================================")

    elif menu == "t":
        print("\nTambah Data")
        nim   = input("NIM        : ")
        nama  = input("Nama       : ")
        uts   = int(input("Nilai UTS  : "))
        uas   = int(input("Nilai UAS  : "))
        tugas = int(input("Nilai Tugas: "))

        akhir = hitung_akhir(tugas, uts, uas)

        data[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }

        print("Data berhasil ditambahkan!")

    elif menu == "u":
        nim = input("Masukkan NIM yang akan diubah: ")
        if nim in data:
            print("Ubah Data untuk", data[nim]["nama"])
            nama  = input("Nama baru       : ")
            uts   = int(input("Nilai UTS baru  : "))
            uas   = int(input("Nilai UAS baru  : "))
            tugas = int(input("Nilai Tugas baru: "))

            akhir = hitung_akhir(tugas, uts, uas)

            data[nim] = {
                "nama": nama,
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Data dengan NIM tersebut tidak ditemukan.")

    elif menu == "h":
        nim = input("Masukkan NIM yang akan dihapus: ")
        if nim in data:
            del data[nim]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan.")

    elif menu == "c":
        nim = input("Masukkan NIM yang dicari: ")
        if nim in data:
            item = data[nim]
            print("\nData ditemukan:")
            print(f"NIM   : {nim}")
            print(f"Nama  : {item['nama']}")
            print(f"Tugas : {item['tugas']}")
            print(f"UTS   : {item['uts']}")
            print(f"UAS   : {item['uas']}")
            print(f"Akhir : {item['akhir']:.2f}")
        else:
            print("Data tidak ditemukan.")

    elif menu == "k":
        print("Program selesai.")
        break

    else:
        print("Menu tidak tersedia!")
