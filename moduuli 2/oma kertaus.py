# if, else, elif
# Tehtävä 1:
# Kysy käyttäjältä luku ja tulosta:
# "Luku on positiivinen" jos > 0
# "Luku on nolla" jos == 0
# "Luku on negatiivinen" jos < 0

luku = float(input("Enter the luku: "))
if luku >= 0:
    print("Luku is positive")
if luku == 0:
    print("Luku is zero")
if luku <= 0:
    print("Luku is negative")

# Tehtävä 2:
# Kysy käyttäjän ikä.
# Jos ikä on vähintään 18 → tulosta "Olet täysi-ikäinen"
# Muuten → "Olet alaikäinen"

ikä = float(input("Kerro ikäsi: "))
if ikä >= 18:
    print("Olet täysi-ikäinen")
else:
    print("Olet alaikäinen")

# Vertailu ja loogiset ehdot
#Tehtävä 3:  kysy kaksi lukua, tulosta isompi

luku1 = float(input("Kerro luku1: "))
luku2 = float(input("Kerro luku2: "))

if luku1 > luku2:
    print(luku1)
if luku1 < luku2:
    print(luku2)

# Tehtävä 4:
# Kysy käyttäjältä salasana.
# Jos salasana on "python123" → "Tervetuloa"
# Muuten → "Väärä salasana"

salasana = (input("Kerro salasana: "))
if salasana == "python123":
    print("Tervetuloa")
else:
    print("Väärä salasana")

# Tehtävä 5 (tärkeä):
# Kysy pistemäärä (0–100).
# Tulosta arvosana:
# 90–100 → 5
# 80–89 → 4
# 70–79 → 3
# 60–69 → 2
# 50–59 → 1
# alle 50 → 0

pisteet = int(input("Anna pistemäärä (0–100): "))

if pisteet >= 90:
    print("5")
elif pisteet >= 80:
    print("4")
elif pisteet >= 70:
    print("3")
elif pisteet >= 60:
    print("2")
elif pisteet >= 50:
    print("1")
else:
    print("0")
