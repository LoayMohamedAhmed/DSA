class Hash_tabel:

    def __init__(self):
        self.hash_tabel = [[]  for i in range(10)]
    
    def hash_function(self, element):
        ch_sum = 0
        for char in element:
            ch_sum+= ord(char)
        return ch_sum % 10
    
    def insert(self , element):
        indx = self.hash_function(element)
        if element not in self.hash_tabel[indx]:
            self.hash_tabel[indx].append(element)

    def search(self, element):
        indx =self.hash_function(element)
        for itr , item in enumerate(self.hash_tabel[indx]):
            if element == item:
                return True, indx, itr
        return False, -1, -1

    def delete(self , element):
        ret ,indx, pos = self.search(element)
        if ret:
            self.hash_tabel[indx].pop(pos)
            print("deleted successfully")
        else:
            print("elemnet not exisit")
    
hashTabel = Hash_tabel()
hashTabel.insert("loay")
hashTabel.insert("bob")
hashTabel.insert("bob")
hashTabel.insert("alice")
print(hashTabel.search("bob")[0])
hashTabel.delete("bob")
print(hashTabel.search("loay")[0])
print(hashTabel.search("bob")[0])