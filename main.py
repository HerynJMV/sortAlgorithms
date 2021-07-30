import numpy as np

# Local imports
from selection import selectionSort
from insertion import insertionSort
from bubble import bubbleSort
from heap import heap
from cocktail import cocktail

list_algorithms = ['Huevo de pascua', 'Selection', 'Insertion',
    'Heap', 'Bubble', 'Cocktail']

def main ():
    n = 10

    while True:
        sort_algorithm = int(input(f'''Bienvenido al algorithm 3000
        Seleccione la opción que desea:
        1. Selection
        2. Insertion
        3. Heap
        4. Bubble
        5. Cocktail
        -1. Salir\n'''))

        if sort_algorithm == -1:
            break

        n = int(input('\nIngrese el tamaño del array: '))

        to_sort = np.random.randint(n, size = n)
        print(f'Array original: {list(to_sort)}')

        if sort_algorithm == 1 :
            sortered = selectionSort(to_sort)

        elif sort_algorithm == 2 :
            sortered = insertionSort(to_sort)

        elif sort_algorithm == 3 :
            sortered = heap(to_sort)

        elif sort_algorithm == 4 :
            sortered = bubbleSort(to_sort)

        elif sort_algorithm == 5 :
            sortered = cocktail(to_sort)

        elif sort_algorithm == 0:
            sortered = 'Hecho por Heryn y Miguel :3'

        print(f'Array ordenado: {sortered} por el algoritmo {list_algorithms[sort_algorithm]}\n')

if __name__ == "__main__":
    main()