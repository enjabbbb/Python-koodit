print("Hello world")

# Lista

luvut = [1,2,3]
print(luvut[0]) #1
print(luvut[1])
print(luvut[2])

#ehtolauseet if, else

ika = 15

if ika >= 15:
    print("olet 0-14-vuotias")
else:
    print("Olet yli 15-vuotias")

#toistorakenteet, for-silmukka
for i in range(5):
    print(i)

# while silmukka

luku = 0
while luku < 5:
    print(luku)
    luku += 1

#funktiot, uudelleenkätettäviä koodipaloja

def tervehdi(nimi):
    print("Huomenta, " + nimi)
    tervehdi("Carrie")

    


