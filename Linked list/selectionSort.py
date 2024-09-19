from SinglyLinkedList import *

class SelectionSort:

    def Sort(self,linked_list):
        current_node = linked_list.head
        for i in range(linked_list.size-1):
            min_val = current_node.data
            next_node = current_node.next
            for itr in range(i,linked_list.size-1):
                if next_node.data < min_val:
                    min_val = next_node.data
                    current_node.data ,next_node.data  = next_node.data , current_node.data
                next_node = next_node.next
            current_node =current_node.next

linked_list = SLinkedList()
selSort = SelectionSort()
linked_list.add(7)
linked_list.add(2)
linked_list.add(1)
linked_list.add(9)
linked_list.add(5)
linked_list.add(21)
selSort.Sort(linked_list)
linked_list.print()   
                