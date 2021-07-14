import numpy as np

# Local imports
from selection import selection, selectionSort

def main ():
    n = 10
    to_sort = np.random.randint(n, size = n)
    selectionSort(to_sort)
    


if __name__ == "__main__":
    main()

