# __init__ (konstruktori)
# __init__ on erikoismetodi joka suoritetaan automaattisesti, kun olio luodaan.
# Sen avulla alustetaan olion attribuutit (eli tiedot)

#esim:

class Koira:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

k = Koira("Musti", 3)

