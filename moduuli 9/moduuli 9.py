# Luo luokka Auto, jossa:
# merkki
# nopeus

class Auto:
    def __init__(self, merkki, nopeus):
        self.merkki = merkki
        self.nopeus = nopeus

    def tulosta_tiedot(self):
        print(f"Merkki: {self.merkki}, Nopeus: {self.nopeus} km/h")

# Luo olio ja tulosta tiedot
auto1 = Auto("Ford", 180)
auto1.tulosta_tiedot()

# Luo 2 eri autoa
auto2 = Auto("Volvo", 160)
auto2.tulosta_tiedot()

#Luo 3 opiskelijaa
#Tulosta tiedot
#Tämä tulee lähes varmasti kokeeseen.

#Luokka opiskelija
class Opiskelija:
    def __init__(self, nimi, pisteet):
        self.nimi = nimi
        self.pisteet = pisteet

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Pisteet: {self.pisteet}")

#3 opiskelijaa
opiskelija1 = Opiskelija("Jere", 100)
opiskelija2 = Opiskelija("Enja", 120)
opiskelija3 = Opiskelija("Kari", 200)
#Tulostus

opiskelija1.tulosta_tiedot()
opiskelija2.tulosta_tiedot()
opiskelija3.tulosta_tiedot()

#Metodit
#Metodi = funktio, joka on määritelty luokan sisällä
#Metodi toimii olioiden kautta: olio voi kutsua metodin, esim. opiskelija1.tulosta_tiedot()
#Jokainen metodi saa self-parametrin automaattisesti, joka viittaa kyseiseen olioon
#Esimerkki: Opiskelija-luokka

class Opiskelija:
    def __init__(self, nimi, pisteet):
        self.nimi = nimi
        self.pisteet = pisteet
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Pisteet: {self.pisteet}")

    def lisaa_pisteita(self, maara):
        self.pisteet += maara

op1 = Opiskelija("Aino", 85)
op1.tulosta_tiedot()        # Tulostaa tiedot
op1.lisaa_pisteita(10)      # Lisää 10 pistettä
op1.tulosta_tiedot()        # Näyttää päivitetyt pisteet

