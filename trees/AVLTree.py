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
        self.height = 0
        self.BF =0
        self.data = data
        self.r_child = None 
        self.l_child = None

class AVL_tree:

    def __init__(self):
        self.root = None
        # define queue help me in insertion
        self.queue = queue.Queue()
    
    
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
    
    def BF_type(self , node):
        # r_type is the type of rotation
        r_type = ""
        # get the first letter of the rotation type based on the balance factor of the current node
        if node.BF > 0:
            r_type += 'R'
        else:
            r_type += 'L'
        # get the second letter of the rotation type  based on the banalnce factor of the child node
        # check the existance of both left and right nodes
        if node.l_child is not None:
            if node.l_child.BF > 0:
                r_type += 'R'
            elif node.l_child.BF < 0:
                r_type += 'L'
        if node.r_child is not None:
            if node.r_child.BF > 0:
                r_type += 'R'
            elif node.r_child.BF < 0:
                r_type += 'L'
        return r_type
    
    # method for rotation to retore the balance of the un-balanced node
    def rotation(self , node ,r_type):
        # node: un-balanced node
        # rtype is: the rotation type
        if r_type == "LL":
            right_childern = node.l_child.r_child
            node.l_child.r_child = node
            node = node.l_child
            node.r_child.l_child =right_childern
        elif r_type == "RR":
            left_children = node.r_child.l_child
            node.r_child.l_child = node
            node = node.r_child
            node.l_child.r_child = left_children
        elif r_type == "LR":
            # left child is right heavy needs a single left rotation
            node.l_child = self.rotation(node.l_child , "RR")
            # the un-balanced node is left heavy and needs a single right rotation
            node = self.rotation(node , "LL")
        else:
            node.r_child = self.rotation(node.r_child , "LL")
            node = self.rotation(node , "RR")
        return node

    def height(self, node):
        if node is None:
            return -1
        l_height = self.height(node.l_child)
        r_height = self.height(node.r_child)
        node.height = max(l_height , r_height)+1
        node.BF = r_height - l_height
        return node.height
    
    # construct an un-balanced binary serch tree
    def add(self, data, node):
        # check the existance of the root node
        if self.root == None:
            self.root = Node(data)
            return self.root , None
        # base case
        if node is None:
            return Node(data) , 0
        
        # initiat the node right and left subtrees height
        # check if the left and right chiderns are exist 
        if node.l_child is not None:
            l_height = node.l_child.height
        else:
            # return -1 as the node doen't have a child 
            l_height = -1
        if node.r_child is not None:
            r_height = node.r_child.height
        else:
            # return -1 as the node doen't have a child 
            r_height = -1
    
        if node.data >= data:
           node.l_child , l_height = self.add(data,node.l_child)
                 
        else:
           node.r_child  , r_height = self.add(data,node.r_child)
        
        
        #get the node height based on the right and left subtrees height
        node.height =max(l_height , r_height) +1
        node.BF = r_height - l_height
        if not -1 <=node.BF <=1:
            #print(node.data)
            rot_type = self.BF_type(node)
            node = self.rotation(node , rot_type)
            node.height = self.height(node)
            #print(rot_type)

        return node , node.height
                
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
            
avl_tree = AVL_tree()
#values = [37,23,46,4,24,38,50,9,32]
for i in range(10):
   avl_tree.root ,_ = avl_tree.add(i, avl_tree.root)
print("BFS........")
avl_tree.BFS()
print("DFS........")
avl_tree.DFS_in_order(avl_tree.root)
value = 25
print("search for "+str(value)+" ......")
print(avl_tree.BST_search(value , avl_tree.root))
print("lowest value is "+ str(avl_tree.lowest_value(avl_tree.root).data))
