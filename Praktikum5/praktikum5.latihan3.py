# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Base case: Saat sudah di elemen terakhir, kembalikan nilainya.
    if index == len(data) - 1:
        return data[index]
        
    # Recursive call: Panggil fungsi lagi untuk mengecek elemen berikutnya.
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa: # membandingkan nilai
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))