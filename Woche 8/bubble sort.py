
array = [1,5,2,8,4,0,3,4,1,52,7,32,21,43,12,5643,123532,214,4325]

def bubbleSort(arr):
    n = len(arr)
    getauscht = False
    for i in range(n-1): #Solange Wiederholen, bis alle in der richtigen Position sind
        for j in range(0, n-i-1): #Tauscht die einzelenen Elemente [3,4,5,1] -> [3,4,1,5]-> [3,1,4,5]
            if arr[j] > arr[j + 1]:
                getauscht = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not getauscht: #Mit dem nächsten Element weitermachen
            continue
    return arr

print(f'Der unsortiere Array: {array}')
bubbleSort(array)
print(f'Der sortierte Array {array}')




