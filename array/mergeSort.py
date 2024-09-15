class mergeSort:

    def Sort(self , F_array, S_array):
        # define sizes and merged array and intialize pointer
        arr1_S , arr2_S =  len(F_array),len(S_array)
        sorted_array = []
        i = j = 0

        while i < arr1_S and j < arr2_S:
            if F_array[i] <= S_array[j]: # add equal to keep stable sorting
                sorted_array.append(F_array[i])
                i+=1
            else:
                sorted_array.append(S_array[j])
                j+=1
        while i < arr1_S:
            sorted_array.append(F_array[i])
            i+=1
        
        while j < arr2_S:
            sorted_array.append(S_array[j])
            j+=1

        return sorted_array
    
    
    def mergesort(self , array):
        # base case
        if len(array) ==1:
            return array
        
        #devide arrays into 2 equal sizes
        mid = len(array)//2
        r_array = array[:mid]
        l_array = array[mid:]
        r_array = self.mergesort(r_array)
        l_array = self.mergesort(l_array)

        sorted_array = self.Sort(r_array,l_array)
        
        return sorted_array
  
mergesort = mergeSort()
unsorted_array = [20,6,61,500,20,30,100,6]
sorted_array = mergesort.mergesort(unsorted_array)
print(sorted_array)


