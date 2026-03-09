def unos(dimenzija, opis):
    print(f"Unesite elemente za {opis} matricu (red po red, odvojeno razmacima!):")
    matrica = []
    for i in range(dimenzija):
        red = input(f"Red {i + 1}: ").split()
        matrica.append([complex(x) for x in red]) 
    return matrica

def sim(matrica):
    dimenzija = len(matrica)
    for i in range(dimenzija):
        for j in range(dimenzija):
            if matrica[i][j] != matrica[j][i]:
                return False
    return True

def antisim(matrica):
    dimenzija = len(matrica)
    for i in range(dimenzija):
        for j in range(dimenzija):
            if matrica[i][j] != -matrica[j][i]:
                return False
    return True

def zbroj(prva, druga):
    dimenzija = len(prva)
    rezultat = [[prva[i][j] + druga[i][j] for j in range(dimenzija)] for i in range(dimenzija)]
    return rezultat

def ispis(matrica, naslov="Rezultat"):
    print(f"\n{naslov}:")
    for red in matrica:
        print(" ".join(str(x) for x in red))

def konacna():
    dimenzija = int(input("Unesite dimenziju kvadratne matrice (n x n): "))

    simetricna = unos(dimenzija, "simetričnu")
    antisimetricna = unos(dimenzija, "antisimetričnu")

    if sim(simetricna) and antisim(antisimetricna):
        originalna = zbroj(simetricna, antisimetricna)
        ispis(originalna, "Originalna matrica")
    else:
        print("\nPogreška! Jedna ili obje matrice ne zadovoljavaju uvjete (simetričnost/antisimetričnost).")

konacna()
