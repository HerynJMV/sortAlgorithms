def circle(A):
    n = len(A)
    print(f'Array Original = {A}')

    # A = [6, 5, 3, 1, 8, 7, 2, 4]
    # n/(2**0) n            [6, 5, 3, 1, 8, 7, 2, 4]
    # n/(2**1) n/2          [4, 2, 3, 1] [8, 7, 5, 6]
    # n/(2**2) n/4          [1, 2][3, 4] [6, 5][7, 8]
    # n/(2**3) paso = n/8   [1][2][3][4] [5][6][7][8]
    # n/(2**4)

    contador = 0
    n_pasos = 1
    paso = n
    while paso > 1:

        ini = 0
        end = paso
        # print(f'{"#"*20}')

        tempList = []
        for i_paso in range(n_pasos):

            # comparar circulos
            tempArray = A[ini: end]
            # print(f'temp Array: {tempArray}')

            for i in range(0, round(len(tempArray)/2) ):

                i_opuesto = - i - 1
                # print(f'iter {contador}, paso {i_paso}, Compara {i} con {i_opuesto}')

                if tempArray[i] > tempArray[i_opuesto]:
                    tempArray[i], tempArray[i_opuesto] = tempArray[i_opuesto], tempArray[i]

            tempList += tempArray
            # print(f'Array = {A}, TempArray {tempArray} ')

            ini += paso
            end += paso

        A = tempList
        contador += 1
        n_pasos = 2**(contador)
        paso = round(n/n_pasos)

    return A


