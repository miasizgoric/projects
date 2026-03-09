import numpy as np

def generiraj_matrice(Z2, n):
    elementi = []
    for i in range(2 ** (n * n)):
        binarno = format(i, f'0{n*n}b')
        matrica = np.array([int(b) for b in binarno]).reshape(n, n)
        elementi.append(matrica)
    return elementi

def generiraj_simetricne(Z2, n):
    matrice = generiraj_matrice(Z2, n)
    return [m for m in matrice if np.array_equal(m, m.T)]

def formatiraj_matrice(naslov, matrice, limit=None):
    rezultat = [f"\n=== {naslov} ===\n"]
    for i, matrica in enumerate(matrice, 1):
        if limit and i > limit:
            rezultat.append(f"... ({len(matrice) - limit} matrica nije prikazano)\n")
            break
        rezultat.append(f"Matrica #{i}:\n")
        rezultat.extend([" ".join(map(str, red)) + "\n" for red in matrica])
        rezultat.append("\n")
    return "".join(rezultat)

def glavni_program():
    Z2 = [0, 1]  

    M2 = generiraj_matrice(Z2, 2)
    S2 = generiraj_simetricne(Z2, 2)

    M3 = generiraj_matrice(Z2, 3)
    S3 = generiraj_simetricne(Z2, 3)

    limit_terminal = 5  

    izlaz = ""
    izlaz += formatiraj_matrice("Elementi M2(Z2)", M2)
    izlaz += formatiraj_matrice("Elementi S2(Z2)", S2)
    izlaz += formatiraj_matrice("Elementi M3(Z2)", M3)
    izlaz += formatiraj_matrice("Elementi S3(Z2)", S3)

    with open("matrice_izlaz.txt", "w") as datoteka:
        datoteka.write(izlaz)

    print(formatiraj_matrice("Elementi M2(Z2)", M2, limit=limit_terminal))
    print(formatiraj_matrice("Elementi S2(Z2)", S2, limit=limit_terminal))
    print(formatiraj_matrice("Elementi M3(Z2)", M3, limit=limit_terminal))
    print(formatiraj_matrice("Elementi S3(Z2)", S3, limit=limit_terminal))
    print("\nCijeli rezultat je spremljen u 'matrice_izlaz.txt'.")

if __name__ == "__main__":
    glavni_program()
