import numpy as np
from numpy.core.numeric import False_
from numpy.lib.function_base import append


def buildMaxHeap (to_sort):

    maxValue = np.max(to_sort)
    indexMaxValue = np.argmax(to_sort)
    rootValue = to_sort[0]

    to_sort[0] = maxValue
    to_sort[indexMaxValue] = rootValue

    return to_sort

def maxHeap (to_sort):

    rootValue = to_sort[0]
    lastBranchValue = to_sort[-1]

    to_sort[0] = lastBranchValue
    to_sort[-1] = rootValue

    # to_sort= np.delete(to_sort, -1)
    
    return to_sort

def heapify (to_sort, order_all = False):
    # Encuentra posición del primero 
    
    indexRootTriad = 0
    indexLastBranch = len(to_sort)

    while True: 
    #for indexRootTriad in range(0,indexLastBranch):

        indexTriad = []
        indexBranchLeft = indexRootTriad + (indexRootTriad + 1) 
        if not indexBranchLeft < indexLastBranch:
            break
            
        indexTriad += [indexRootTriad, indexBranchLeft]

        indexBranchRight =  indexBranchLeft + 1
        if indexBranchRight < indexLastBranch:
            indexTriad += [indexBranchRight]

        triad = np.take(to_sort, indexTriad)

        maxValueTriad = np.max(triad)
        maxIndexTriad = indexTriad[np.argmax(triad)] 

        if maxIndexTriad != indexRootTriad:

            rootTriadValue = to_sort[indexRootTriad]

            print(
                f"Intercambia el {rootTriadValue} "
                f"con el {maxValueTriad} de la triada {indexRootTriad}")

            to_sort [indexRootTriad] = maxValueTriad
            to_sort [maxIndexTriad] = rootTriadValue

            print(to_sort)
        

        if order_all:
            indexRootTriad += 1
        elif maxIndexTriad != indexRootTriad:
            indexRootTriad = maxIndexTriad
        else:
            break
    
    return to_sort


def heap(to_sort):
    to_sort = heapify(to_sort, order_all=True)
    longitud = len(to_sort)
    order = []
    for mimiguelito in range(0, longitud):
        print(f'Iteracion numero {mimiguelito}, longitud to_sort {len(to_sort)}')
        to_sort = buildMaxHeap(to_sort)
        to_sort = maxHeap(to_sort)
        print('Antes de mimiguelito ',to_sort)
        order.append(to_sort[-1])
        to_sort = to_sort[:-1] 
        print('Despues de mimiguelito ',to_sort)

        to_sort = heapify(to_sort, order_all=False)

    print(order)

if __name__ == "__main__":

    # n = 9
    # to_sort = np.random.randint(n, size = n)
    # print(f'Array original: {to_sort}')
    # perro = buildMaxHeap(to_sort)
    # print(f'buildMaxHeap: {perro}')

    # gato = maxHeap(to_sort)
    # print(f'MaxHeap: {gato}')

    arr = [29, 40, 14, 72, 14, 23, 40, 31, 80]


    heap(arr)