import random

def arvo_luku():
    return random.randint(1, 13)

def tervehdi(tervehdys):
    kerrat = arvo_luku()
    for i in range(kerrat):
        print(tervehdys + " " + str(i + 1) + ". kerran")
    return

tervehdi("Moikka")

käyttäjä = input('Anna nimesi: ')
print("Hauska tavata, " + käyttäjä + "!")
