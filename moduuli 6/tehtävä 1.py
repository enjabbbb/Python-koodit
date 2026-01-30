import random

def roll_dice():
    return random.randint(1, 6)

while True:
    silmaluku = roll_dice()
    print(silmaluku)
    if silmaluku == 6:
        break