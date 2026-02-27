# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        if "0" in hasil and "1" in hasil and "2" in hasil: # caranya adalah dengan menambahkan fungsi if dengan maksud bahwa setiap pin harus 3 angka yang berbeda
            print("PIN:", hasil)
            return
        return
    
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)
buat_pin(3)

