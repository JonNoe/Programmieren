import numpy as np

arr = np.array([1,2,3,4,5,6])
x= arr.copy()
y = arr.view()
arr[0] = 10

print(f'Orginaler array: {arr} \n')

print(f'Der kopierte array: {x}')
print(f'{x.base} -> Der kopierte array hat keine Werte zugeordnet\n')

print(f'Der array der angeschaut wird: {y}')
print(f'{y.base} -> Der kopierte array hat  Werte zugeordnet\n')


#Array reshapen von 1d - 2d
arr[0] = 1
zweid = arr.reshape(2,3)
print(zweid)
print(f'{zweid} -> Der Array hat Werte im speicher -> view\n')

#zusammenführen von arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#2*1D = 1D 
#machen beide das gleiche
arr_join = np.concatenate((arr1,arr2))
print(arr_join)

arr_rows = np.hstack((arr1, arr2))
print(arr_rows)

#2*1D = 2D
#machen beide das gleiche
arr_stack = np.stack((arr1,arr2))
print(arr_stack)

arr_lines = np.vstack((arr1,arr2))
print(arr_lines)

#Teilen
arr_geteilt = np.split(arr,2)
print(arr_geteilt)
print(arr_geteilt[0])
print(arr_geteilt[1])

#Suchen in array
suche = np.where(arr == 1)
print(suche)
x = np.searchsorted(arr, [5,3,7])
print(x)

#Filterarray
start = np.array([1,2,3,4,5,6,7,8,9])
filter_array = []

for element in start:
    if element % 2 == 0:
        filter_array.append(True)
    else:
        filter_array.append(False)

ende = start[filter_array]
print(ende)