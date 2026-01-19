nimi = input("Anna nimi: ")

if nimi == "Enja":
    print("Syötteeksi annettiin Enja")

suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari==räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")


ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if (ikä >= 18 or ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")


    kaffepaussi = True

    if kaffepaussi == True:
        print("Pidetään kahvitauko")

kahvi_on_hyvää = True
kahvikone_kahvi_on_hyvää = False
if kahvi_on_hyvää == True and kahvikone_kahvi_on_hyvää == False:
    print("Olet varmaan karamalmin kampuksella")

if kahvi_on_hyvää == False or kahvikone_kahvi_on_hyvää == False:
    print("Or loooginen operaattori")

    ikä = float(input("Anna ikä: "))
    nimi = input("Anna nimi: ")

    if ikä > 18 or ikä  < 40 and nimi == "Enja":
        print("Ikä on 18 ja 40 välillä, ei sisällä 18 eikä 40")

        if not False:
            print("False ei ole tosi")






