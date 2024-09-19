from SinglyLinkedList import *

class SelectionSort:

    def Sort(self,linked_list):
        current_node = linked_list.head
        for i in range(linked_list.size-1):
            min_val = current_node.data
            next_node = current_node.next
            for itr in range(itr,linked_list.size):
                if next_node.data < min_val:
                    min_val = next_node.data
                    current_node.data = min_val
                next_node = next_node.next
            current_node =current_node.next
    
                