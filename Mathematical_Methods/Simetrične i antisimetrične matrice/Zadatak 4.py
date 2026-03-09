import numpy as np

def bazaKompleksnogProstora(n):
    baza = []
    for i in range(n):
        for j in range(n):
            matrica = np.zeros((n, n), dtype=complex)
            matrica[i, j] = 1
            baza.append(matrica)
    return baza

def bazaRealnogProstora(n):
    baza = []
    for i in range(n):
        for j in range(n):
            matrica = np.zeros((n, n))
            matrica[i, j] = 1
            baza.append(matrica)
    for i in range(n):
        for j in range(n):
            matrica = np.zeros((n, n), dtype=complex)
            matrica[i, j] = 1j
            baza.append(matrica)
    return baza

n = int(input("Unesite dimenziju matrice n: "))
vektorskiProstor = input("Unesite 'C' za kompleksni prostor ili 'R' za realni prostor: ").strip().upper()

if vektorskiProstor == 'C':
    baza = bazaKompleksnogProstora(n)
    print(f"Kanonska baza za M_{n}(C) kao kompleksni prostor:")

elif vektorskiProstor == 'R':
    baza = bazaRealnogProstora(n)
    print(f"Kanonska baza za M_{n}(C) kao realni prostor:")

for matrica in baza:
    print(matrica, "\n")
