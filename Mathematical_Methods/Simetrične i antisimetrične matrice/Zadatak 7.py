import random

def realna(dimenzija):
    matrica = [[0.0 for _ in range(dimenzija)] for _ in range(dimenzija)]
    for i in range(dimenzija):
        for j in range(i):
            vrijednost = random.uniform(-10, 10)
            matrica[i][j] = vrijednost
            matrica[j][i] = -vrijednost
    return matrica

def kompleksna(dimenzija):
    matrica = [[0 + 0j for _ in range(dimenzija)] for _ in range(dimenzija)]
    for i in range(dimenzija):
        for j in range(i):
            realni_dio = random.uniform(-10, 10)
            imaginarni_dio = random.uniform(-10, 10)
            vrijednost = complex(realni_dio, imaginarni_dio)
            matrica[i][j] = vrijednost
            matrica[j][i] = -vrijednost
    return matrica

def ispis(matrica):
    for redak in matrica:
        print(" ".join(
            f"{element.real:5.1f}+{element.imag:5.1f}j" if isinstance(element, complex)
            else f"{element:5.1f}" for element in redak
        ))
        
print("Realni antisimetrični prostori")
for dimenzija in range(1, 11):
    print(f"Antisimetrična matrica za realni vektorski prostor A_n(C), n = {dimenzija}:")
    matrica = realna(dimenzija)
    ispis(matrica)
    print()

print("Kompleksni antisimetrični prostori")
for dimenzija in range(1, 11):
    print(f"Antisimetrična matrica za kompleksni vektorski prostor A_n(C), n = {dimenzija}:")
    matrica = kompleksna(dimenzija)
    ispis(matrica)
    print()
