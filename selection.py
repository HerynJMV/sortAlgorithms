import numpy as np

n = 10
to_sort = np.random.randint(9, size = 10)


for index_to_sort, value_to_sort in enumerate(to_sort):

    minimum_index = index_to_sort
    minimum_value = value_to_sort

    print(f'Lista desordenada: {to_sort}')
    array_disorderly = to_sort[index_to_sort + 1:]
    print(f'rango azul {array_disorderly}')
    for item_index , item_value in enumerate(array_disorderly):    
        
        if item_value < minimum_value :

            minimum_value = item_value
            minimum_index = item_index + (index_to_sort + 1)

    print(f'Posición del minimo actual: {minimum_index}, Current minimum {minimum_value}' )
    # Asignar el valor de la posción 0 a la posición del minimo valor encontrado (minimun_index)

    # Intercambiar el valor min encontrado (minimum_value) con el de la posción 0
    to_sort[minimum_index] = value_to_sort
    to_sort[index_to_sort] = minimum_value

    print(f'Iteracion # {index_to_sort}: {to_sort} \n')


