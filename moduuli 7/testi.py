nimet = ("Juha, Matti")

print(nimet[0])
print(nimet[1])
print(nimet[2])

nimet2 = ("Ei Juha" , nimet[1])

print(nimet2[0])

print(len(nimet))

hedelmät = "banaani", "omena", "tomaatti"
(eka, toka, kolmas) = hedelmät
eka = hedelmät[0]
toka = hedelmät[1]
kolmas = hedelmät[2]

print(hedelmät[0])

print(nimet)

# monikko funktion paluuarvona

import random

def heitä():
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    return eka, toka

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")
