#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling (Studi Kasus)
#Latihan Dasar 1 : Membuat fungsi Load Data dari File
#=========================================================================

#variabel meyimpan data file
nama_file = "data mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}
    with open("data mahasiswa.txt","r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            data_dict[nim] = {"Nama" :  nama, "Nilai" : int(nilai)}
        return data_dict

# buka_data = baca_data(nama_file)
#print(len(buka_data))

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling (Studi Kasus)
#Latihan Dasar 2 : Membuat fungsi menampilkan data
#=========================================================================

def tampilkan_data(data_dict):
    print("\n=====Daftar Mahasiswa====")
    print(f"{"NIM" : <10} | {'Nama' : <12} | {'Nilai' :>5}")
    #:<10 artinya rata kiri dengan lebar kolom 10 karakter
    print("-"*32) #membuat garis
    
    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['Nama']
        nilai = data_dict[nim]['Nilai']
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

# tampilkan_data(buka_data)

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling (Studi Kasus)
#Latihan Dasar 3 : Membuat fungsi mencari data
#=========================================================================

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingim anda cari").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]['Nama']
        nilai = data_dict[nim_cari]['Nilai']

        print("===Data Mahasiswa Ditemukan===")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan")

# cari_data(buka_data)

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling (Studi Kasus)
#Latihan Dasar 4 : Membuat fungsi update data
#=========================================================================

#buat fungsi update data
def ubah_data(data_dict):

    #awali dengan cari nim/data mahasiswa yang ingin diupdate
    nim = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim not in data_dict:
        print('Data tidak ditemukan')
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru ").strip())
    except ValueError:
        print('Nilai harus berupa angka')

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100")

    nilai_lama = data_dict[nim]['Nilai']
    data_dict[nim]['Nilai'] = nilai_baru

    print("Update berhasil dari", nilai_lama, "Menjadi", nilai_baru)

# ubah_data(buka_data)

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling (Studi Kasus)
#Latihan Dasar 5 : Membuat fungsi meyimpan data
#=========================================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file,"w",encoding='utf-8') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['Nama']
            nilai = data_dict[nim]['Nilai']
            file.write(f"{nim},{nama},{nilai}\n")

# simpan_data(nama_file, buka_data)
# print("Data berhasil tersimpan")

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling (Studi Kasus)
#Latihan Dasar 5 : Membuat Menu Interaktif
#=========================================================================

def main():
    #Load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) #fs.1

    while True:
        print("===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke FIle")
        print("0. Keluar")

        pilihan = input("Pilih menu :")

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            print("Program selesai")
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()