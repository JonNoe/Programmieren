
def mergesort (arr):
    
    if len(arr) > 1:

        array_left = arr[:len(arr)//2]
        array_right = arr[len(arr)//2:]

        mergesort(array_left)
        mergesort(array_right)
        
        i = 0 #Index von array_left
        j = 0 #Index von array_rigth
        
        k = 0 #Index von array_merged
        
        while i < len(array_left) and j < len(array_right):
            if array_left[i] < array_right[j]:
                arr[k] = array_left[i]
                i += 1
            else:
                arr[k] = array_right[j]
                j += 1       
            k += 1  
            
        while i < len(array_left):
            arr[k] = array_left[i]
            i += 1
            k += 1
            
        while j < len(array_right):
            arr[k] = array_right[j]
            j += 1
            k += 1

array = [1,5,2,8,4,0,3,4,1,52,7,32,21,43,12,5643,123532,214,4325]
print(f'Der unsortiere Array: {array}')
mergesort(array)
print(f'Der sortierte Array {array}')


