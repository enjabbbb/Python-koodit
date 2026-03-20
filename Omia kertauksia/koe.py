from enum import nonmember

luvut = []
for i in range(5):
    luku = float(input(f"Anna luku {i+1}: "))
    luvut.append(luku)

keskiarvo = sum(luvut) / len(luvut)
print("Keskiarvo on:", keskiarvo)

suurin = None

while True:
    luku = float(input("Anna luku (0 lopettaa): "))

    if luku == 0:
        break

    if suurin is None or luku > suurin:
        suurin = luku

if suurin is None:
    print("Et antanut yhtään lukua.")
else:
    print("Suurin annettu luku on:", suurin)


