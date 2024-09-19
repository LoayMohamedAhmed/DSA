class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self,data):
        if self.head== None:
            node = Node(data)
            self.head = node
            self.tail = self.head
        elif self.head == self.tail:
            node = Node(data)
            self.head.next = node
            self.tail = node
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        self.size+=1

    def insert(self, val, pos):
        if pos> self.size:
            return False
        new_node = Node(val)
        if pos ==0:
            new_node.next = self.head
            self.head = new_node
            self.size+=1
            return True
        current_node = self.head
        for i in range(1,pos):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.size+=1
        return True

        


    def lowest_val(self):
        l_val = self.head.data
        current_node = self.head.next
        while current_node != None:
            if current_node.data < l_val:
                l_val = current_node.data
            current_node =current_node.next
        return l_val
        
    
    def print(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp = temp.next
    
    def delet_val(self,val):
        if self.head.data == val:
            self.head = self.head.next
            self.size-=1
            return True
        current_node = self.head.next
        prv_node = self.head
        while current_node != None:
            if current_node.data == val:
                prv_node.next = current_node.next
                self.size-=1
                return True
            prv_node = current_node
            current_node =current_node.next
        return False

'''''
L_list = SLinkedList()
L_list.add(5)
L_list.add(6)
L_list.add(12)
L_list.add(1)
L_list.insert(3,3)
L_list.delet_val(1)
L_list.print()
print(L_list.lowest_val())
'''