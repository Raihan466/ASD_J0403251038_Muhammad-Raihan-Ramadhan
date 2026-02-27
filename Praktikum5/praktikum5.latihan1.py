# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
    # Base case
    if n == 0: #berhenti ketika n = 0
        return 1 #jika n = 0, maka balik nilai ke 1
    
    # Recursive case
    return a * pangkat(a, n - 1) #jika tidak sama dengan 1, maka jalankan fungsi return ini sampai n = 0 
print(pangkat(2, 4))

# pangkat(2,4)
# = 2 * pangkat(2,3)
# = 2 * (2 * pangkat(2,2))
# = 2 * (2 * (2 * pangkat(2,1)))
# = 2 * (2 * (2 * (2 * pangkat(2,0))))
# = 2 * 2 * 2 * 2 * 1
# = 16