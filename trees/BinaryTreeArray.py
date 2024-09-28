##################################################################
#..................... Array implementation ................... ##
##################################################################

class B_tree:
    def __init__(self):
        self.array = []
    # return the index of the right child
    def r_index(self, index):
        return 2*index + 2
    
    # return the index of the left child
    def l_index(self , index):
        return 2*index +1
    
    def add(self, data):
        self.array.append(data)

    # return the children of some node 
    def find_children(self , index):
        return self.l_index(index), self.r_index(index)

    def DFS_pre_order(self,index):
        if len(self.array)== 0:
            return
        if index >= len(self.array):
            return
        print(self.array[index])
        self.DFS_pre_order(self.l_index(index))
        self.DFS_pre_order(self.r_index(index))

b_tree = B_tree()
for i in range(9):
    b_tree.add(i)
print("DFS........")
b_tree.DFS_pre_order(0)
        
