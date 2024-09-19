from SinglyLinkedList import *

class BubbleSort:

    def Sort(self, linkedList):
        sorted = False
        for i in range(linkedList.size-1):
            if not sorted:
                sorted = True
                current_node = linkedList.head
                next_node = current_node.next
                for itr in range(linkedList.size-i-1):
                    if current_node.data > next_node.data:
                        current_node.data , next_node.data = next_node.data , current_node.data
                        sorted = False
                    current_node = next_node
                    next_node = next_node.next
            else:
                break

linked_list = SLinkedList()
bubSort = BubbleSort()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)
linked_list.add(21)
bubSort.Sort(linked_list)
linked_list.print()
