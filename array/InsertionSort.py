class insertionSort:
    def Sort(self , array):
        arrSize = len(array)
        for loops in range(1,arrSize):
            current_indx = loops
            for itr in range( loops-1 , -1, -1):
                if array[current_indx] < array[itr]:
                    array[itr] , array[current_indx] = array[current_indx] , array[itr]
                    current_indx = itr
                else:
                    break
        return array

inserSort = insertionSort()
unsorted_array = [7,12,9,11,3]
sorted_array = inserSort.Sort(unsorted_array)
print(sorted_array)
