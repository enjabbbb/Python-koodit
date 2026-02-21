# funktion rakenne

#def funktion_nimi(parametrit):
    # funktion runko
    #"return paluuarvo

#def kertoo, että nyt määritellään funktio

#funktion nimi on itse keksitty

#sulkeissa ovat parametrit (eli tiedot, jotka funktio tarvitsee)

#return palauttaa tuloksen takaisin pääohjelmalle
#funktio nimeltä tervehdi joka tulostaa hei maailma ja palauttaa sen
def tervehdi():
    print("Hei maailma!")
# pääohjelma
tervehdi()

#Tee funktio tervehdi_nimea(nimi), joka tulostaa:
#Hei <nimi>!
#Kutsu funktiota käyttäjän syötteellä (input).


def tervehdi_nimea(nimi):
    print("Hei, " + nimi + "!")

kayttajan_nimi = input("Anna nimesi: ")
tervehdi_nimea(kayttajan_nimi)

#Tee funktio nelio(luku), joka tulostaa luvun neliön.
#Esim:
#nelio(4) → 16


#tehdään funktio
def nelio(luku):
    print(luku ** 2)

# esimerkki kutsu
nelio(3)
