import numpy as np

def selectionSort(to_sort):
    print(f'Array desordenado: {to_sort}')
    for index_to_sort, value_to_sort in enumerate(to_sort):

        print(f'Array en ordenamiento: {to_sort}')
        array_disorderly = to_sort[index_to_sort + 1:]
        print(f'rango desordenado {array_disorderly}')

        if len(array_disorderly) == 0:
            break

        minimum_value = np.min(array_disorderly)
        index_minimum_value = np.argmin(array_disorderly) + (index_to_sort + 1)

        if value_to_sort < minimum_value:
            minimum_value = value_to_sort
            index_minimum_value = index_to_sort

        print(f'Posición y valor del minimo en el rango desordenado: {index_minimum_value}, {minimum_value}' )
        # Asignar el valor de la posción 0 a la posición del minimo valor encontrado (minimun_index)

        # Intercambiar el valor min encontrado (minimum_value) con el de la posción 0
        to_sort[index_minimum_value] = value_to_sort
        to_sort[index_to_sort] = minimum_value

        print(f'Iteracion # {index_to_sort}: {to_sort} \n')
    return to_sort
