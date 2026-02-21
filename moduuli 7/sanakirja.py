opiskelija = {
    "nimi": "matti",
    "ika": 21,
    "pisteet": 85
}
#Tulosta nimi
#Tulosta pisteet
print(opiskelija["nimi"])
print(opiskelija["pisteet"])

#Muuta pisteitä ja tulosta uusi arvo

opiskelija["pisteet"] = 100
print(opiskelija["pisteet"])

#Lisätään uusi avain sanakirjaan, kurssi
opiskelija["kurssi"] = "Python"
print(opiskelija)

for avain in opiskelija:
    print(avain)

#Python oletusarvoisesti iteroi sanakirjan avaimet.

