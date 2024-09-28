import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Stack_queue import queue
class Node:
    def __init__(self , data):
        self.data = data
        self.r_child = None 
        self.l_child = None

class B_tree:

    def __init__(self):
        self.root = None
        # define queue help me in insertion
        self.queue = queue.Queue()
    
    def add(self ,data):
        # create new node
        new_node = Node(data)
        # check if the tree has root node 
        if self.root == None:
            self.root = new_node
            # add the new node to the queue
            self.queue.enqueue(new_node)
            return
        # every time get the first node in the queue in order to fill the tree level by level like BFS
        current_node =self.queue.peek()
        if current_node.l_child == None:
            self.queue.peek().l_child = new_node
            self.queue.enqueue(new_node)
        elif current_node.r_child == None:
            self.queue.peek().r_child = new_node
            self.queue.enqueue(new_node)
            # if the current node has left and right childs remove it
            self.queue.dequeue()
        return
    
    def BFS(self):
          # create queue to contain nodes
          BFS_queue =queue.Queue()
          BFS_queue.enqueue(self.root)
          while not BFS_queue.is_empty():
                current_node =BFS_queue.dequeue()
                print(current_node.data)
                if current_node.l_child != None:
                    BFS_queue.enqueue(current_node.l_child)
                if current_node.r_child != None:
                    BFS_queue.enqueue(current_node.r_child)

    def DFS_pre_order(self, node ):
        if node == None:
            return
        print(node.data)
        self.DFS_pre_order(node.l_child)
        self.DFS_pre_order(node.r_child)
            

b_tree = B_tree()
for i in range(9):
    b_tree.add(i)
print("BFS........")
b_tree.BFS()
print("DFS........")
b_tree.DFS_pre_order(b_tree.root)
