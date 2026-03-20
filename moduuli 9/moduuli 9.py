# Luokka, olio ja alustaja

# Olio-ohjelminnissa luokalla tarkoitetaan yleiskäsitettö, joka määrittää yleiset ja yhteiset piirteet, joita sen jäsenillä on

# pienin mahd. Koira-luokka:

class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi


koira = Koira()
koira.nimi = "Rekku"
koira.syntymävuosi = 2022

print(f"{koira.nimi} on syntynyt vuonna {koira.syntymävuosi}.")

