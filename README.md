#🟦 1. Dictionary untuk menyimpan data mahasiswa
data = {}


Variabel data adalah dictionary kosong yang nanti akan menyimpan seluruh data mahasiswa.
Struktur penyimpanan:

data = {
   'NIM123': {
       'nama': 'Budi',
       'tugas': 80,
       'uts': 85,
       'uas': 90,
       'akhir': 86.75
   },
   ...
}

#🟦 2. Fungsi menghitung nilai akhir
def hitung_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)


Fungsi ini menghitung nilai akhir dengan bobot:

Tugas = 30%

UTS = 35%

UAS = 35%

#🟦 3. Perulangan utama program
while True:


Program berjalan terus sampai pengguna memilih menu Keluar (K/k).

#🟦 4. Menu pilihan

Program menampilkan menu:

(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar


Setelah itu input menu diproses:

menu = input("Pilih menu : ").lower()


.lower() digunakan agar input huruf besar/kecil tetap diterima.

#🟦 5. Menu L — Lihat Data
if menu == "l":


Menampilkan tabel data yang rapi dan rata tengah.

Judul tabel dicetak seperti ini:

print(f"| {'NO':^2} | {'NAMA':^12} | {'NIM':^12} | {'TUGAS':^5} | {'UTS':^4} | {'UAS':^4} | {'AKHIR':^7} |")


:^12 → rata tengah lebar 12

:^5 → rata tengah lebar 5

Jika data kosong:

if len(data) == 0:
    print("|                     TIDAK ADA DATA                               |")


Jika ada data, dilakukan looping:

for nim, item in data.items():


item adalah dictionary data mahasiswa.

Cetak setiap baris:

print(f"| {no:^2d} | {nim:^12s} | {item['nama']:^12s} | "
      f"{item['tugas']:^5d} | {item['uts']:^4d} | {item['uas']:^4d} | "
      f"{item['akhir']:^7.2f} |")

#🟦 6. Menu T — Tambah Data
elif menu == "t":


Input dari user:

NIM

Nama

Nilai Tugas

Nilai UTS

Nilai UAS

Lalu nilai akhir dihitung:

akhir = hitung_akhir(tugas, uts, uas)


Data disimpan dalam dictionary:

data[nim] = {
    "nama": nama,
    "tugas": tugas,
    "uts": uts,
    "uas": uas,
    "akhir": akhir
}

#🟦 7. Menu U — Ubah Data
elif menu == "u":


Cek apakah NIM ada dalam dictionary:

if nim in data:


Jika ada, data diinput ulang seperti Tambah Data.

Jika tidak ditemukan → muncul pesan:

print("Data dengan NIM tersebut tidak ditemukan.")

#🟦 8. Menu H — Hapus Data
elif menu == "h":


Hapus data berdasarkan NIM:

del data[nim]


Jika tidak ada → tampilkan pesan data tidak ditemukan.

#🟦 9. Menu C — Cari Data
elif menu == "c":


Mencari data berdasarkan NIM.

Jika ditemukan, tampilkan:

NIM
Nama
Nilai tugas
Nilai UTS
Nilai UAS
Nilai akhir


Jika tidak → tampilkan "Data tidak ditemukan."

#🟦 10. Menu K — Keluar Program
elif menu == "k":
    print("Program selesai.")
    break


break menghentikan loop while True.

🟦 11. Jika input menu tidak valid
else:
    print("Menu tidak tersedia!")
