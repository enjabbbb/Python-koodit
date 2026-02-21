# Tulosta luvut 1-10 käyttäen while-silmukkaa

luku = 1
while luku <= 10:
    print(luku)
    luku = luku + 1

# sama takaperin

luku = 10
while luku >= 1:
    print(luku)
    luku = luku - 1


# Kysy käyttäjältä lukua niin kauan kunnes hän antaa luvun 0.
# Tulosta jokainen annettu luku.

luku = int(input("Anna luku: "))

while luku != 0:
    print("Annoit luvun:", luku)
    luku = int(input("Anna luku:" ))

print("Ohjelma päättyi.")

#Tehtävä 4 (todella tärkeä):
#Kysy käyttäjältä lukuja ja laske niiden summa.
#Kun käyttäjä antaa 0 → lopeta ja tulosta summa.

summa = 0
luku = int(input("Anna luku: "))

while luku != 0:
    summa = summa + luku
    luku = int(input("Anna luku: "))

print("Summa on: ", summa)
















