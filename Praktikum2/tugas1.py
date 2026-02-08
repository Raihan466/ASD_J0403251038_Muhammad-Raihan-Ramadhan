# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Muhammad Raihan Ramadhan
# NIM : J0403251038
# Kelas : A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "Stok_Barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_data(nama_file):
    data_dict = {}
    with open("Stok_Barang.txt","r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            data_dict[kode] = {"nama" : nama, "stok" : int(stok)}
        return data_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

def simpan_data(nama_file, data_dict):
    with open(nama_file,"w",encoding='utf-8') as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]['nama']
            stok = data_dict[kode]['stok']
            file.write(f"{kode},{nama},{stok}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

def tampilkan_data(data_dict):
    print('=====Data Barang=====')
    print(f"{"kode" :<10} | {"nama" :<12} | {"stok" :>5}")
    print("-"*30)

    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]['nama']
        stok = data_dict[kode]['stok']
        print(f"{kode:<10} | {nama:<12} | {stok:>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------

def cari_barang(data_dict):
    kode_cari = input("Masukkan kode barang: ").strip()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        stok = data_dict[kode_cari]['stok']

        print("===Barang Ditemukan===")
        print(f"kode : {kode_cari}")        
        print(f"nama : {nama}")
        print(f"stok : {stok}")
    else:
        print('Barang tidak ditemukan')

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(data_dict):
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang baru: ").strip()

    if kode in data_dict:
        print("Kode barang", kode, "sudah ada, silakan ulangi dengan input kode lain")
        return

    stok_awal = int(input("Masukkan jumlah stoknya: "))

    if stok_awal < 0:
        print("error")
        return

    data_dict[kode] = {
        'nama': nama,
        "stok": stok_awal
    }
       
# -------------------------------
# Fungsi: Update stok barang
# -------------------------------

def ubah_data(data_dict):
    kodebarang = input('Masukkan kode barang yg ingin diubah stoknya: ').strip()

    if kodebarang in data_dict:
        nama = data_dict[kodebarang]['nama']
        stok = data_dict[kodebarang]['stok']

        print("===Barang Ditemukan===")
        print(f"kode : {kodebarang}")        
        print(f"nama : {nama}")
        print(f"stok : {stok}")
    else:
        print("Barang tidak ditemukan")
        return
    
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = int(input("Masukkan pilihan 1 atau 2: "))
    jumlah = int(input("Masukkan jumlahnya: "))

    if pilihan < 1 or pilihan > 2:
        print("Error")

    if jumlah < 0:
        print("Error")

    stok = data_dict[kodebarang]['stok']

    if pilihan == 1:
        stok_baru = stok + jumlah
        data_dict[kodebarang]['stok'] = stok_baru
        print("Stok berhasil ditambahkan, stok dari:", stok, "menjadi:", stok_baru)
    elif pilihan == 2:
        stok_baru = stok - jumlah
        data_dict[kodebarang]['stok'] = stok_baru
        print("Stok berhasil dikurangkan, stok dari:", stok, "menjadi:", stok_baru)

# -------------------------------
# Program Utama
# -------------------------------
def main():
# Membaca data dari file saat program mulai
    buka_data = baca_data(nama_file)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu :")

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_barang(buka_data)
        elif pilihan == "3":
            tambah_barang(buka_data)
        elif pilihan == "4":
            ubah_data(buka_data)
        elif pilihan == "5":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            print("Program selesai")
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
