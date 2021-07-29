
def bubbleSort (A):
    n = len(A)

    while n >= 0 :

        for i in range(0, n - 1):
            
            if A[i] > A[i + 1] :
                A[i], A[i + 1] = A[i + 1], A[i]
        
        n -= 1
    return A



