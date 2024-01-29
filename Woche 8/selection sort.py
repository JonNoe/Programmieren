
array = [1,5,2,8,4,0,3,4,1,52,7,32,21,43,12,5643,123532,214,4325]

def selectionSort(arr):
    n = len(arr)
    for i in range(n): #geht jede Position durch 
        position = i
        for j in range(i+1,n): #geht jede Position durch, die auf i folgt
            if arr[j] < arr[position]:
                position = j #Wenn Wert von j kleiner als bei position = i dann wird die position dieser Wert und überprüft wieder ob der nächste Kleiner ist
        
        arr[i], arr[position] = arr[position], arr[i]   # An der stelle von i wird der kleinste gefundene Wert eingesetzt und das gegenstück an der Position von diesem


print(f'Der unsortiere Array: {array}')
selectionSort(array)
print(f'Der sortierte Array {array}')




