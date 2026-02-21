lista = [3,7,2,9,5]
print(lista[0])
print(lista[4])

for luku in lista:
    print(luku)

#Tulosta lukujen summa käymällä lista läpi silmukassa.
#tee summamuuttuja ennen silmukkaa
#lisää jokainen luku siihen


luvut = [3, 7, 2, 9, 5]

summa = 0

for luku in luvut:
    summa = summa + luku

print("Lukujen summa on:", summa)

#Luo tyhjä lista.
#Kysy käyttäjältä 5 lukua ja lisää ne listaan append()-metodilla.
#Tulosta lopuksi lista.

#tyhjä lista
luvut = []

#kysytään 5 lukua
for i in range(5):
    luku = int(input("Anna luku: "))
    luvut.append(luku)

#tulostus
print(luvut)

#Laske käyttäjän antamien lukujen keskiarvo.
#Tarvitset:
#summan
#listan pituuden len() avulla

#luodaan tyhjä lista
luvut = []
# kysytään käyttäjältä 5 lukua
for i in range(5):
    luku = float(input("Anna luku: "))
    luvut.append(luku)


#lasketaan summa ja keskiarvo
summa = sum(luvut)
keskiarvo = summa / len(luvut)

#tulostus
print("Lukujen keskiarvo on:", keskiarvo)












