class HashMap:

    def __init__(self):

        self.bucket = [[]  for i in range(10)]

    def hash_function(self,number):
        power = 1
        sum =10
        while number//10 !=0:
            num = int((number/10**power - number//10**power)*10)
            sum+=num
            number/=10
        return sum %10
    
    def search(self , element):
        index = self.hash_function(element)
        for itr ,item in enumerate(self.bucket[index]):
            if item[0]==element:
                return item ,True , index , itr
        return "not found",False , -1 ,-1
    
    def insert(self, element):
        index = self.hash_function(element[0])
        _,ret, indx , pos = self.search(element[0])
        if ret:
            self.bucket[index][pos] = element
        else:
            self.bucket[index].append(element)
        
    def delete(self, element):
        _,ret, indx , pos = self.search(element)
        if ret:
            self.bucket[indx].pop(pos)
            print("deleted successfully")
        else:
            print("elemnet not exisit")

hashTabel = HashMap()
hashTabel.insert([12345,"loay"])
hashTabel.insert([12345,"loay mohamed"])
hashTabel.insert([56862,"bob"])
hashTabel.insert([56862,"bob"])
hashTabel.insert([20013,"alice"])
print(hashTabel.search(12345)[0])
hashTabel.delete(56862)
print(hashTabel.search(20013)[0])
print(hashTabel.search(56862)[0])
        
