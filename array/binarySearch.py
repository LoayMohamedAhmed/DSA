class BinarySearch:
    # implementation with loop
    def Search2(self,array, value):
        left =0
        right = len(array)
        while left <= right:
            mid = (left+ right)//2
            if array[mid] == value:
                break
            elif array[mid] > value:
                right = mid-1
            else:
                left = mid+1
        if left > right:
            mid = -1
        return mid

    # implementation with recursion
    def Search1(self, array , value, left=0 ,right=None):
        # base case
        if right!=None and left > right :
            return -1
        # first run check
        if right == None:
            right = len(array)

        mid = (left+right)//2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            indx = self.Search1(array,value,left,mid-1)
        else:
            indx = self.Search1(array , value , mid+1, right)
        return indx
    
binarySearch = BinarySearch()
unsorted_array = [ 2, 3, 7, 7, 11, 15, 25]
index = binarySearch.Search2(unsorted_array,11)

print(index)
