import numpy as np

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

    return to_sort

def heapify (to_sort, order_all = False):
    # Encuentra posición del primero 
    
    indexRootTriad = 0
    indexLastBranch = len(to_sort)

    while True: 
    
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
            to_sort [indexRootTriad] = maxValueTriad
            to_sort [maxIndexTriad] = rootTriadValue

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
    for i in range(0, longitud):
        
        to_sort = buildMaxHeap(to_sort)
        to_sort = maxHeap(to_sort)
        
        order.append(to_sort[-1])
        to_sort = to_sort[:-1]

        to_sort = heapify(to_sort, order_all=False)

    return order