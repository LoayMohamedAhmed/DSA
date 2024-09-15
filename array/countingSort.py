import numpy as np
class CountingSort:

    def Sort(self, array):
        h_value = 0
        sorted_array = []
        # find the heighest value 
        for element in array:
            if h_value < element:
                h_value = element

        #create counting array with h_elements
        counting_array = np.zeros(h_value+1, dtype=np.int32)

        #count the repetation of each element of the un sorted array
        for element in array:
            counting_array[element]+=1
        
        #recreate the array with sorted elements
        for indx , value in enumerate(counting_array):
            for i in range(value):
                sorted_array.append(indx)
        
        return sorted_array

countSort = CountingSort()
unsorted_array = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sorted_array = countSort.Sort(unsorted_array)
print(sorted_array)