class SelectionSort:

    def Sort(self , array):
        arrSize = len(array)
        for loops in range(arrSize-1):
            minIndx = loops
            for itr in range(loops+1 , arrSize):
                if array[minIndx] > array[itr]:
                    minIndx = itr
            array[minIndx] , array[loops] = array[loops] ,array[minIndx]
        return array
    
selSort = SelectionSort()
unsorted_array = [7,12,9,11,3]
sorted_array = selSort.Sort(unsorted_array)
print(sorted_array)
