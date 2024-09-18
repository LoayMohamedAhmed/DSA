class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head

        elif self.head == self.tail:
            self.head.next = Node(data)
            self.tail = self.head.next
            self.tail.prev = self.head

        else:
            self.tail.next = Node(data)
            temp = self.tail
            self.tail =self.tail.next
            self.tail.prev =temp

    def print(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp = temp.next

    def print_rev(self):
        temp = self.tail
        while temp!= None:
            print(temp.data)
            temp = temp.prev
Dlist = DLinkedList()
Dlist.add_node(5)
Dlist.add_node(6)
Dlist.add_node(12)
Dlist.print()
Dlist.print_rev()
