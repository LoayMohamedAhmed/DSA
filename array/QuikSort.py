class QuickSort:

    def Sort(self , array , i,j):
        # i  indicate the start of array 
        # j  indicate the end of array
        if i>=j:
            return
        pivot = j
        start = i
        end = j-1
        while True:
            if array[start] <= array[pivot] and start< pivot:
                start +=1
            elif array[end] > array[pivot] and end>0:
                end -=1
            elif start < end:
                array[start] , array[end] = array[end] , array[start]
            elif start >= end:
                break
        array[pivot] , array[start] = array[start] , array[pivot] # always start stand on number bigger than the pivot 
        #pivot = start
        self.Sort(array, i,start-1)
        self.Sort(array, start+1 , j)
        return array

quicksort = QuickSort()
unsorted_array = [3, 7, 8, 5, 2, 1, 9, 5, 4]
sorted_array = quicksort.Sort(unsorted_array,0,len(unsorted_array)-1)
print(sorted_array)