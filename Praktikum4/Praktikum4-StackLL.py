#================================================
#Nama   : Muhammad Raihan Ramadhan
#NIM    : J0403251038
#Kelas  : A2
#================================================


#================================================
#Implementasi dasar : Stack
#================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan niai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal = none)

#Stack ada operasi push (memasukkan head baru) dan pop (menghapus head)

class Stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def is_empty(self):
        return self.top is None #stack kosong jika top = none

    def push(self, data): #memasukkan data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class node
    
        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #mengambil / menghapus node paling atas (top/head)

        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next
        return data_terhapus
        
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print ("Top", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
print("Peek (lihat top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (lihat top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (lihat top): ", s.peek())
