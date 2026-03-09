import numpy as np

def realnaKanonskaBazaSnC(n):
    baza = []
    for i in range(n):
        matrica = np.zeros((n, n), dtype=int)
        matrica[i][i] = 1
        baza.append(matrica.tolist())
    return baza

def kompleksnaKanonskaBazaSnC(n):
    baza = []
    for i in range(n):
        for j in range(i, n):
            matrica = np.zeros((n, n), dtype=complex)
            matrica[i][j] = 1 + 0j
            matrica[j][i] = 1 + 0j
            baza.append(matrica)

    for matrica in baza:
        for red in matrica:
            print(" ".join(map(str, map(int, red.real))))
        print()

def main():
    print("Realni vektorski prostor")
    for i in range(1, 11):
        print(f"Kanonska baza za Sn(C) realni vektorski prostor n = {i}")
        baza = realnaKanonskaBazaSnC(i)
        for matrica in baza:
            for red in matrica:
                print(" ".join(map(str, red)))
            print()

    print("Kompleksni vektorski prostor")
    for i in range(1, 11):
        print(f"Kanonska baza za Sn(C) kompleksni vektorski prostor n = {i}")
        kompleksnaKanonskaBazaSnC(i)
        print()
main()