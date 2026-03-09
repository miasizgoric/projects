def matrice(mat):
    size = len(mat)
    
    simetricna = [[0] * size for _ in range(size)]
    antisimetricna = [[0] * size for _ in range(size)]
    
    kompleksna = any(isinstance(mat[i][j], complex) for i in range(size) for j in range(size))
    
    for i in range(size):
        for j in range(size):
            if kompleksna:
                simetricna[i][j] = (mat[i][j] + mat[j][i].conjugate()) / 2
                antisimetricna[i][j] = (mat[i][j] - mat[j][i].conjugate()) / 2
            else:
                simetricna[i][j] = (mat[i][j] + mat[j][i]) / 2
                antisimetricna[i][j] = (mat[i][j] - mat[j][i]) / 2
    
    print("\nSimetrični dio matrice:")
    for row in simetricna:
        print(row)
    print("\nAntisimetrični dio matrice:")
    for row in antisimetricna:
        print(row)

matA = [
    [4, 6, -7, 2, 1],
    [0, -4, 2, 1, 1],
    [-2, 3, 5, 9, -3],
    [6, 6, 7, -8, -2],
    [8, 8, 2, 0, -5]
]
matrice(matA)

matB = [
    [1+1j, 3-2j, 4+5j, 2j],
    [1-1j, 3+2j, 7, 2-1j],
    [5+5j, -5+8j, 10, 1j],
    [-1+1j, 3+2j, 0, 5j]
]
matrice(matB)
