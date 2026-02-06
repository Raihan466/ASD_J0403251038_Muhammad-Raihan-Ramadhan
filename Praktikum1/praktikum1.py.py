#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#=========================================================================


print("====Membuka file dalam satu string===")
with open("data mahasiswa.txt","r",encoding="utf-8") as file: #buka file dgn mode read
    isi_file = file.read() #mengambil data dan menyimpan semua data dlm 1 varianel str yg panjang
print(isi_file)

print("Tipe Data :", type(isi_file))

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 2 : 
#=========================================================================

print("====Membuka file per baris===")
jumlah_baris = 0
with open("data mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter enter (baris baru)
        print('baris ke-', jumlah_baris)
        print("isinya ", baris)

#Parsing baris menjadi data satuan dan menampilkan dalam bentuk kolom2 data
with open("data mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter enter (baris baru)
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("NIM :", nim, "Nama :", nama, "Nilai :", nilai) #menampilkan satuan data dlm bentuk kolom

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 3 : Membaca data dan menyimpannya ke struktur data list
#=========================================================================

data_list = [] #inisialisasi list untuk menampung data

with open("data mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter enter (baris baru)
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #menyimpan data ke list
print("===menampilkan list===")
print(data_list)
print("Contoh record ke-1", data_list[0])
print("Contoh record ke-2", data_list[1])

print("Jumlah record", len(data_list))

#=========================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 4 : Membaca data dan menyimpannya ke struktur dictionary
#=========================================================================

data_dict = {} #Inisialisasi Dictionary

with open("data mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter enter (baris baru)
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #Simpan data dalan dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("===Menampilkan Data Dictionary===")
print(data_dict)

