import numpy as np

def bazaHermitska(n):
    baza = []
    for i in range(n):
        for j in range(n):
            matrica = np.zeros((n, n), dtype=complex)
            if i == j:
                matrica[i, j] = 1
            else:
                matrica[i, j] = 1
                matrica[j, i] = np.conj(matrica[i, j])
            baza.append(matrica)
    return baza

for n in range(1, 11):
    print("---------------------------------------------------------")
    print(f"Kanonska baza za H_{n}:")
    baza = bazaHermitska(n)
    for matrica in baza:
        print(matrica)
        print()
