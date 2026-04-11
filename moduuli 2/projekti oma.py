# kivi paperi ja sakset peli

import random

vaihtoehdot = ["kivi", "paperi", "sakset"]

while True:
    pelaaja = input("Valitse kivi, paperi tai sakset (tai 'lopeta'): ").lower()

    if pelaaja == "lopeta":
        print("Peli päättyi!")
        break

    if pelaaja not in vaihtoehdot:
        print("Virheellinen valinta.")
        continue

    kone = random.choice(vaihtoehdot)
    print("kone valitsi:", kone)
    if pelaaja == kone:
        print("Tasapeli")
    elif (
        (pelaaja == "kivi" and kone == "sakset") or
        (pelaaja == "paperi" and kone == "kivi") or
        (pelaaja == "sakset" and kone == "paperi")
         ):
        print("Voitit!")
    else:
        print("Hävisit!")