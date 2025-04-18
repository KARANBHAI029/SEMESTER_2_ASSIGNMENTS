import numpy as np

def generate_magic_square(n):
    if n % 2 == 1:  
        magic_square = np.zeros((n, n), dtype=int)
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i, j] = num
            i, j = (i - 1) % n, (j + 1) % n
            if magic_square[i, j]: 
                i = (i + 2) % n
                j = (j - 1) % n
        return magic_square
    elif n % 4 == 0:  
        magic_square = np.arange(1, n*n + 1).reshape(n, n)
        mask = np.array([[((i // (n//2) + j // (n//2)) % 2 == 0) for j in range(n)] for i in range(n)])
        magic_square[mask] = n*n + 1 - magic_square[mask]
        return magic_square
    else: 
        return "Not implemented"

for N in range(4, 9):
    print(f"Magic Square for N={N}:\n", generate_magic_square(N), "\n")
