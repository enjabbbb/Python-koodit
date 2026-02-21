# Tehtävä 6:
# Kysy käyttäjältä lämpötila.
# Jos lämpötila on yli 20 JA alle 30 →
# tulosta "Hyvä kesäsää"
# Muuten → "Ei kesäsää"

temperature = float(input("Anna lämpötila: "))
if temperature > 20 and temperature < 30:
    print("Hyvä kesäsää")
else:
    print("Ei kesäsää")

# Tehtävä 7:
# Kysy käyttäjältä viikonpäivä.
# Jos päivä on "lauantai" TAI "sunnuntai" →
# tulosta "Viikonloppu!"
# Muuten → "Arkipäivä"

day = input("Anna viikonpäivä: ")
if day == "lauantai" or day == "sunnuntai":
    print("viikonloppu!")
else:
    print("Arkipäivä")

# Tehtävä 8 (tee ilman apua):
# Kysy käyttäjältä ostoksen summa.
# Jos summa:
# yli 100 € → anna 20 % alennus
# yli 50 € → anna 10 % alennus
# muuten → ei alennusta
# Tulosta lopullinen hinta.

summa = float(input("Mikä on ostoksen summa: "))
if summa > 100:
    alennus = summa * 0.20
elif summa > 50:
    alennus = summa * 0.10
else:
    alennus = 0
lopullinen_hinta = summa - alennus
print("Lopullinen hinta:", lopullinen_hinta)

