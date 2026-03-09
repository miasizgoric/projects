import numpy as np

matrica_A = np.array([
    [4, 6, -7, 2, 1],
    [0, -4, 2, 1, 1],
    [-2, 3, 5, 9, -3],
    [6, 6, 7, 8, -2],
    [8, 8, 2, 0, -5]
], dtype=float)

matrica_B = np.array([
    [1 + 1j, 3 - 2j, 4 + 5j, 0 + 2j],
    [1 - 1j, 3 + 2j, 7 + 0j, 2 - 1j],
    [5 + 5j, -5 + 8j, 10 + 0j, 0 + 1j],
    [-1 + 1j, 3 + 2j, 0 + 0j, 0 + 5j]
], dtype=complex)

def hermitski_dio(matrica):
    if np.isrealobj(matrica):
        transponirana = matrica.T
        hermitski = 0.5 * (matrica + transponirana)
    else:
        konjugirano_transponirana = np.conjugate(matrica.T)
        hermitski = 0.5 * (matrica + konjugirano_transponirana)
    return hermitski

def anti_hermitski_dio(matrica):
    if np.isrealobj(matrica):
        transponirana = matrica.T
        antihermitski = 0.5 * (matrica - transponirana)
    else:
        konjugirano_transponirana = np.conjugate(matrica.T)
        antihermitski = 0.5 * (matrica - konjugirano_transponirana)
    return antihermitski


hermitski_A = hermitski_dio(matrica_A)
antihermitski_A = anti_hermitski_dio(matrica_A)

hermitski_B = hermitski_dio(matrica_B)
antihermitski_B = anti_hermitski_dio(matrica_B)

print("Hermitski dio matrice A:")
print(hermitski_A)
print("\n")

print("Anti-Hermitski dio matrice A:")
print(antihermitski_A)
print("\n------------------------------------------")

print("Hermitski dio matrice B:")
print(hermitski_B)
print("\n")

print("Anti-Hermitski dio matrice B:")
print(antihermitski_B)
print("\n")