#Kysy käyttäjältä 5 lukua while-silmukan avulla.
#Laske niiden keskiarvo.

summa = 0
laskuri = 0

while laskuri < 5:
    luku = float(input("Anna luku: "))
    summa = summa + luku
    laskuri = laskuri + 1

keskiarvo = summa / 5
print("Keskiarvo on:", keskiarvo)

# Kysy käyttäjältä salasanaa niin kauan kunnes hän kirjoittaa "ok".
# Tulosta lopuksi "Salasana oikein".

salasana = ""

while salasana != "ok":
    salasana = input("Anna salasana: ")

print("Salasana oikein")

#Kysyy käyttäjältä lukuja.
#Jos luku on negatiivinen → tulosta "Negatiivinen luku"
#Jos luku on positiivinen → lisää se summaan.
#Lopeta kun käyttäjä antaa 0.
#Tulosta positiivisten lukujen summa.

summa = 0

while True:
    luku = float(input("Anna luku (0 lopettaa): "))

    if luku == 0:
        break
    elif luku < 0:
        print("Negatiivinen luku")
    else:
        summa = summa + luku

print("Positiivisten lukujen summa on:", summa)
