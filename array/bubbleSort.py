class BubbleSort :

    def Sort(self,array):
        sortedF = False
        arrSize = len(array)
        for loops in range(arrSize-1):
            if not sortedF:
                sortedF = True
                for itr in range(arrSize - loops-1):
                    if array[itr] > array[itr+1]:
                        sortedF = False
                        array[itr],array[itr+1] = array[itr+1],array[itr]
            else:
                break
        return array

bubSort = BubbleSort()
unsorted_array = [7,12,9,11,3]
sorted_array = bubSort.Sort(unsorted_array)
print(sorted_array)