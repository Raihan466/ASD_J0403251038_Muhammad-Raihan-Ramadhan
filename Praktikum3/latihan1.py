class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
       

class DoublyLinkedlist :
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def	delete_node(self, key):
        temp = self.head
        if temp and temp.data == key :
            self.head = temp.next
            temp = None
            return 
    
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print('Null')
    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

dll = DoublyLinkedlist()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)

dll.display_forward()
dll.display_backward()
