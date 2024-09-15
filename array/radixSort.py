class RadixSort:

    def Sort(self,array):
        bucket = [[],[],[],[],[],[],[],[],[],[]]
        h_num = 0
        d = 1 # d is the number of digits

        # find the heighest number
        for element in array:
            if h_num < element:
                h_num = element

        # find d
        while int(h_num/10) !=0:
            h_num /=10
            d+=1
        
        #start radix algorithm
        for i in range(1 , d+1):
            while len(array)>0:
                element = array.pop(0)
                temp = element/10**i
                num = int((temp-int(temp))*10)
                bucket[num].append(element)

            for item in bucket:
                while len(item)>0:
                    array.append(item.pop(0))
        
        return array

radixSort = RadixSort()
unsorted_array = [20,6,61,500]
sorted_array = radixSort.Sort(unsorted_array)
print(sorted_array)
