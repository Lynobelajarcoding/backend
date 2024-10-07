def hitung_gaji(nama, golongan, jam_kerja):
    if golongan == "A":
        upah_per_jam = 5000
    elif golongan == "B":
        upah_per_jam = 7000
    elif golongan == "C":
        upah_per_jam = 8000
    elif golongan == "D":
        upah_per_jam = 10000
    else:
        return "Golongan tidak valid"

    if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
    else:
        uang_lembur = 0

    upah = upah_per_jam * jam_kerja
    gaji = upah + uang_lembur
    
    return gaji

nama_karyawan = input("Masukkan nama Karyawan: ")
golongan = input("Masukkan Golongan (A/B/C/D): ")
jumlah_jam_kerja = int(input("Masukkan jumlah jam kerja: "))

gaji_karyawan = hitung_gaji(nama_karyawan, golongan, jumlah_jam_kerja)

print()
print("## Program Python Menghitung Gaji Karyawan ##")
print("=============================================")
print()
print("Nama Karyawan: ", nama_karyawan)
print("Golongan: ", golongan)
print("Jumlah jam kerja: ", jumlah_jam_kerja)
print()
print(nama_karyawan, "menerima upah Rp. ", gaji_karyawan, "per minggu")