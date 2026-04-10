# __init__ (konstruktori)
# __init__ on erikoismetodi joka suoritetaan automaattisesti, kun olio luodaan.
# Sen avulla alustetaan olion attribuutit (eli tiedot)

#esim:

class Koira:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

k = Koira("Musti", 3)

#Useampi olio + lista

#Luo lista opiskelijoista
#Käy lista läpi for-silmukalla
#Tulosta kaikkien tiedot

#Luodaan luokka opiskelija
class Opiskelija:
    def __init__(self, nimi, ika, kurssi):
        self.nimi = nimi
        self.ika = ika
        self.kurssi = kurssi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Ika: {self.ika}, Kurssi: {self.kurssi}")

#Lista opiskleijaolioista

opiskelijat = [
    Opiskelija("Enja", 19, "Ohjelmointi"),
    Opiskelija("Jere", 20,"Fysiikka"),
    Opiskelija("Kari", 8, "Tietokannat")

]

#Käydään lista läpi for-silmukalla ja tulostetaan

for opiskelija in opiskelijat:
    opiskelija.tulosta_tiedot()