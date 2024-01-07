import numpy as np

def nulldimensional():
    arr= np.array(42)
    print(arr)
    print(f'Der array hat die {arr.ndim}. Dimension')   

def eindimensional():
    arr = np.array([1,2,3,4,5])

    for i in range(len(arr)):
        print(arr[i])
    print(f'Der array hat die {arr.ndim}. Dimension')

def zweidimensional():
    arr = np.array([[1,2,3],[4,5,6]])
    print(arr)
    print(f'Der array hat die {arr.ndim}. Dimension')    
def dreidimesnionsal():
    arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
    print(arr)
    print(f'Der array hat die {arr.ndim}. Dimension')    
def vierdimensional():
    arr = np.array([1,2,3,4,5], ndmin=4)
    print(arr)
    print(f'Der array hat die {arr.ndim}. Dimension')

dimension = int(input('Wieviele dimensionen soll der array haben? '))

if dimension == 0:
    nulldimensional()
if dimension == 1:
    eindimensional()
if dimension == 2:
    zweidimensional()
if dimension == 3:
    dreidimesnionsal
if dimension == 4:
    vierdimensional()



