#================================================
#Nama   : Muhammad Raihan Ramadhan
#NIM    : J0403251038
#Kelas  : A2
#================================================


#================================================
#Implementasi dasar : Queue
#================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan niai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal = none)

class queue:
    #buat konstruktor untuk inisialisasi variabel front and rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None
    
    #membuat fungsi untuk menambahkan data baru pada bagian belakang
    def enqueue(self,data):
        nodeBaru = Node(data)

        #Jika queueu kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru setelahnya rear
        self.rear = nodeBaru #jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan/front
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None
        return data_terhapus
    
    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print(" Rear")

#instansiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()