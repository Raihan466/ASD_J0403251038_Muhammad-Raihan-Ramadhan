def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
alist=[43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
shortBubbleSort(alist)

# Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
# skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
print(alist[:5])

# Kandidat berapa saja yang lolos?
print("Kandidat yang lolos:")
for nilai in alist[:5]:
    kandidat = alist.index(nilai) + 1
    print("Kandidat ke-", kandidat, "dengan nilai", nilai)