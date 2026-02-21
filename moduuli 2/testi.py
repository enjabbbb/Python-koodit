luku = float(input("Anna luku: "))
if luku % 2 == 0:
    print("Luku on parillinen")
else:
    print("Luku on pariton")

luku = 1
summa = 0
while luku <= 10:
    summa = summa + luku
    luku = luku +1

print("Summa on", summa)


lista = [6, 7, 6, 9]
for arvo in lista:
    print(arvo)

def pienempi(a, b):
    if a < b:
        return a
    else:
        return b