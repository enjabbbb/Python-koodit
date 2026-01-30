import random

def roll_dice(sides):
    return random.randint(1, sides)

max_sides = int(input("Anna nopan tahkojen määrä: "))

while True:
    silmaluku = roll_dice(max_sides)
    print(silmaluku)
    if silmaluku == max_sides:
        break