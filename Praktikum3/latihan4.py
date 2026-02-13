class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
        
    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = other_list.head

ll1 = LinkedList()
ll1.insert_at_end(1)
ll1.insert_at_end(3)
ll1.insert_at_end(5)
ll1.insert_at_end(7)

ll2 = LinkedList()
ll2.insert_at_end(2)
ll2.insert_at_end(4)
ll2.insert_at_end(6)
ll2.insert_at_end(8)

print("Linked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

ll1.merge(ll2)

print("Linked List setelah digabungkan:")
ll1.display()
