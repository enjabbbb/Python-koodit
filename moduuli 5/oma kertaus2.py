#Käy lista läpi ja etsi:
#suurin luku
 #pienin luku
#Tulosta molemmat lopuksi.
#Vinkki:
#aseta alkuarvoksi listan ensimmäinen luku
#vertaa sitä muihin silmukassa
#Tämä on erittäin klassinen ohjelmointitehtävä.

#lista
luvut = [3,7,2,9,5]

# asetetaan alkuarvot listan ensimmäisen luvun perusteella
suurin = luvut[0]
pienin = luvut[0]

#käydään lista läpi
for luku in luvut:
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku
#tulostetaan tulokset
print("Suurin luku on: ", suurin)
print("Pienin luku on:", pienin)


#Kysyy käyttäjältä 5 lukua → tallentaa listaan
#Tulostaa kaikki luvut
#Laskee summan
#Tulostaa keskiarvon
#Ilmoittaa suurimman luvun

luvut = []
#kysy 5 lukua
for i in range(5):
    luku = float(input("Anna luku: "))
    luvut.append(luku)

#tulosta kaikki luvut
print("Antamasi luvut:", luvut)
#summa
summa = sum(luvut)
#keskiarvo
keskiarvo = summa / len(luvut)

#etsi suurin luku
suurin = luvut[0]
for luku in luvut:
    if luku > suurin:
        suurin = luku

#tulostukset
print("summa:", summa)
print("keskiarvo:", keskiarvo)
print("suurin luku:", suurin)

