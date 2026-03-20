nimet = []
etunimi = input("Anna ensimmäinen etunimi tai lopeta painamalla enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava etunimi tai lopeta painamalla enter:")

for nimi in nimet:
    print(f"Moi, {nimi}!")