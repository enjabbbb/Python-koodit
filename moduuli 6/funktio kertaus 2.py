#Tee funktio summa(a, b), joka palauttaa lukujen summan return-lauseella.
#Tulosta funktion palauttama arvo ohjelmassa.

#Funktio ja return lause
def summa(a, b):
    return a + b
#tulosta
tulos = summa(248547, 5984)
print(tulos)

 #tee funktio onko_parillinen(luku)
#palauttaa True jos luku on parillinen
#muuten False
#Käytä funktiota if-ehdossa.

def onko_parillinen(luku):
    if luku % 2 == 0:
        return True
    else:
        return False

luku = int(input("Anna luku: "))
if onko_parillinen(luku):
    print("Luku on parillinen.")
else:
    print("Luku on pariton.")



#Tee funktio laske_summa(lista), joka:
#käy listan läpi
#palauttaa summan
#Kokeile funktiota listalla:
#[4, 7, 1, 9]

def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

luvut = [4, 7, 1, 9]
tulos = laske_summa(luvut)
print(tulos)

#Tee funktio keskiarvo(lista), joka palauttaa listan keskiarvon.
#Tulosta keskiarvo pääohjelmassa.



def keskiarvo(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Pääohjelma
luvut = [3, 5, 8, 10]
ka = keskiarvo(luvut)
print("Listan keskiarvo on:", ka)













