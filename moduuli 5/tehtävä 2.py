luvut = []

while True:
    syote = input("Enter a number: ")
    if syote == "":
        break
    luku = float(syote)
    luvut.append(luku)

luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]

print("The greatest numbers in descending order:")
for luku in viisi_suurinta:
    print(luku)
