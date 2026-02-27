# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)

# Base case: Jika panjang string = n, maka cetak hasil dan berhenti
# recursive call: Tambahkan "A" dan "B" lalu panggil fungsi lagi
# jika panjang hasil belum 2 maka lanjut ke cabang A dan B, A didahulukan karena ditulis terlebih dahulu
# 1. hasil masih kosong, maka langsung isi "A", tapi panjang masih satu maka buka lagi cabangnya isi "A"... didapat kombinasi pertama "AA"
# 2. Karena A yang kedua sudah maka kita hentikan kemudian lanjut ke B, jadi "AB"
# 3. A awal pertama sudah dipakai, maka hentikan kemudian kita lanjut ke B