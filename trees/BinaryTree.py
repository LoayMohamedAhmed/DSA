##################################################################
#.................... pointer implementation .................. ##
##################################################################
import sys
import os
import random

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
    
    # search ffor valise in BST
    def BST_search(self , value , node):
        if node == None:
            return str(value)+ " is not found"
        
        if node.data == value:
            return str(value)+ " is found"
        
        if node.data > value:
            message = self.BST_search(value , node.l_child)
        else:
            message = self.BST_search(value , node.r_child)
        
        return message
        
    # construct an un-balanced binary serch tree
    def add_BST(self, data, node):
        # check the existance of the root node
        if self.root == None:
            self.root = Node(data)
            return
        if node is None:
            return Node(data)
        
        if node.data >= data:
           node.l_child = self.add_BST(data,node.l_child)
                 
        else:
           node.r_child = self.add_BST(data,node.r_child)

        return node
                
    #find the lowest value
    def lowest_value(self, node):
        if node is None or node.l_child is None :
            return node
        return self.lowest_value(node.l_child)
    
    def delete(self,data,node):
        # base case to return if the node is not found
        if node is None:
            return
        
        # check if the target value is the root node
        if self.root.data == data:
            # find the lowest value for the right branch and store it in LV_node
            # the lowest value of the right branch is already greater than any value of the left subtree of the root node
            LV_node = self.lowest_value(self.root.r_child)
            # if there's no right child then replace the left node with the root
            if LV_node is not None:
                LV_node.l_child = self.root.l_child
                self.root = self.root.r_child
            else:
                self.root = self.root.l_child
            return
        # start searching for target value
        if node.data > data:
            node.l_child = self.delete(data, node.l_child)
        elif node.data < data:
            node.r_child = self.delete(data, node.r_child)
        else:
            # if it's found then find the lowest value of it's right branch like what have done with the root node
            LV_node =self.lowest_value(node.r_child)
            if LV_node is not None:
                LV_node.l_child = node.l_child
                node = node.r_child
            else:
                node = node.l_child
        return node
    
    # implement breadth fist search
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

    def DFS_in_order(self, node ):
        if node == None:
            return
        self.DFS_in_order(node.l_child)
        print(node.data)
        self.DFS_in_order(node.r_child)
            

b_tree = B_tree()
values = [37,23,46,4,24,38,50,9,32]
for i in range(9):
    b_tree.add_BST(values[i],b_tree.root)
print("BFS........")
b_tree.BFS()
print("DFS........")
b_tree.DFS_in_order(b_tree.root)
value = 25
print("search for "+str(value)+" ......")
print(b_tree.BST_search(value , b_tree.root))
print("lowest value is "+ str(b_tree.lowest_value(b_tree.root).data))
b_tree.delete(90,b_tree.root)
print("DFS........")
b_tree.DFS_in_order(b_tree.root)
