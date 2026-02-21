# 1. Luo tyhjä lista
luvut = []

# 2. Kysy käyttäjältä lukuja (0 lopettaa)
luku = int(input("Anna luku (0 lopettaa): "))

while luku != 0:
    # 3. Lisää luku listaan
    luvut.append(luku)
    luku = int(input("Anna luku (0 lopettaa): "))

# 4. Funktio, joka laskee listan summan
def laske_summa(lista):
    summa = 0
    for x in lista:
        summa += x
    return summa

# 5. Funktio, joka laskee keskiarvon
def keskiarvo(lista):
    if len(lista) == 0:
        return 0
    return laske_summa(lista) / len(lista)

# 6. Etsi suurin arvo for-silmukalla
def suurin_arvo(lista):
    if len(lista) == 0:
        return None
    suurin = lista[0]
    for x in lista:
        if x > suurin:
            suurin = x
    return suurin

# 7. Tulosta kaikki tulokset selkeästi
print("\n--- Tulokset ---")
print("Annoit luvut:", luvut)
print("Summa:", laske_summa(luvut))
print("Keskiarvo:", keskiarvo(luvut))
print("Suurin arvo:", suurin_arvo(luvut))











