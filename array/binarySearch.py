class BinarySearch:
    # implementation with loop
    # def Search2(self,array, value):
    #     left =0
    #     right = len(array)-1
    #     while left <= right:
    #         mid = (left+ right)//2
    #         if array[mid] == value:
    #             break
    #         elif array[mid] > value:
    #             right = mid-1
    #             mid =-1
    #         else:
    #             left = mid+1
    #             mid =-1
    #     #if left > right:
    #     #   mid = -1
    #     return mid
    def Search2(self , array , value):
        ref = 0
        idx = -1
        while len(array)>=1:
            mid = len(array)//2
            if array[mid] == value:
                idx = ref+mid
                break
            elif len(array) == 1:
                break
            elif array[mid] > value:
                array = array[:mid]
            else:
                array = array[mid+1 : ]
                ref += (mid+1)
        return idx   

    # implementation with recursion
    # def Search1(self, array , value, left=0 ,right=None):
    #     # base case
    #     if right!=None and left > right :
    #         return -1
    #     # first run check
    #     if right == None:
    #         right = len(array)

    #     mid = (left+right)//2
    #     if array[mid] == value:
    #         return mid
    #     elif array[mid] > value:
    #         indx = self.Search1(array,value,left,mid-1)
    #     else:
    #         indx = self.Search1(array , value , mid+1, right)
    #     return indx
    def Search1(self,array,value,ref):
        # get the index of mid value
        mid = len(array)//2 
        if array[mid] == value:
            return ref+mid
        # the mid is -1 if the array length is 1
        if mid ==0:
            return -1
        
        if array[mid]> value:
            idx =self.Search1(array[:mid],value,ref)
        else:
            idx = self.Search1(array[mid+1:] ,value,ref+mid+1)
        return idx
    
binarySearch = BinarySearch()
unsorted_array = [ 2, 3, 7, 7, 11, 15, 25]
index = binarySearch.Search2(unsorted_array,2)

print(index)
