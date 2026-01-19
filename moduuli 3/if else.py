ikä = float(input("Anna ikä: "))

if ikä >= 18:
    print("Olet täysi-ikäinen")
else:
    print("Et ole täysi-ikäinen")

ikä = int(input("Anna ikäsi: "))
if ikä >= 65:
    print("Olet eläkeiässä.")
elif ikä >= 18:
    print("Olet työiässä.")
elif ikä >= 7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")