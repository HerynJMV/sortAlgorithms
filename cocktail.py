def cocktail (A):
    n = len(A)
    x = 0
    while x < n :

        print(f'n = {n}, x = {x}\n')

        # style to print bars with the number size
        for valor in A:
            print(f"{'|'*valor}")
        
        # left to right
        for i in range(x, n - 1):
            
            if A[i] > A[i + 1] :
                A[i], A[i + 1] = A[i + 1], A[i]
        n -= 1
        
        # right to left
        for i in range(n - 1, x, -1):

            if A[i] < A[i - 1] :
                A[i], A[i - 1] = A[i - 1], A[i]
        x += 1

        # print(f"{'#'*70} \n")

    return A
