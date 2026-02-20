#================================================
#Nama   : Muhammad Raihan Ramadhan
#NIM    : J0403251038
#Kelas  : A2
#================================================

#================================================
#Implementasi dasar : node pada linked list
#================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan niai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal = none)

#1) mebuat node debgan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2)Mendefinisikan head Menghubung Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Traversal : Menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node selanjutnya



