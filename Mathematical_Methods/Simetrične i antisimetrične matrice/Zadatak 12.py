import numpy as np

def antihermitske(n):
    baze = []

    for i in range(n):
        for j in range(n):
            matrica = np.zeros((n, n), dtype=complex)
            if i == j:
                matrica[i, j] = 1j
            elif i < j:
                matrica[i, j] = 1 + 1j
                matrica[j, i] = -np.conj(matrica[i, j])
            baze.append(matrica)

    return baze

def ispis(matrice):
    for index, matrica in enumerate(matrice):
        print(f"Matrica {index + 1}:")
        print(np.array_str(matrica, precision=2, suppress_small=True))
        print()

def main():
    for n in range(1, 11):
        print(f"Kanonske baze za skup antihermitskih matrica reda n = {n}:")
        baze = antihermitske(n)
        ispis(baze)
        print("-" * 50)

if __name__ == "__main__":
    main()
