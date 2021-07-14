import numpy as np

def insertionSort(to_sort):
    print(f'Array original: {to_sort}\n')
    
    for index, value in enumerate(to_sort):
        
        newIndexToValue = index

        while value < to_sort[newIndexToValue - 1]  and newIndexToValue > 0:
            to_sort[newIndexToValue] = to_sort[newIndexToValue - 1]  
            to_sort[newIndexToValue - 1] = value
            newIndexToValue -= 1 
            print(f'Así va el array: {to_sort}')