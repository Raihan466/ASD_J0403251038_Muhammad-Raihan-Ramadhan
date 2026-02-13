class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return

            temp = temp.next

            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

    def display(self):
        if not self.head:
            print("List kosong")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("... (kembali ke head)")

cll = CircularSinglyLinkedList()

cll.insert_at_end(3)
cll.insert_at_end(7)
cll.insert_at_end(12)
cll.insert_at_end(19)
cll.insert_at_end(25)

cll.display()

cll.search(12)   # ditemukan
cll.search(100)
