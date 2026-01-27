nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print(nimet[3])
print(nimet[1])
print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)
print (len(nimet))

print("Nimet alkiosta 1 alkioon 3")
print(nimet[1:3])
print(nimet[:3])


nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(len(nimet))

nimet = []

nimi = input ("Anna nimi: ")

while nimi != "":

    nimet.append(nimi)

    nimi = input("Anna nimi: ")

    print(nimet)

    for n in nimet:
        print(f"Moi, {n}!")
