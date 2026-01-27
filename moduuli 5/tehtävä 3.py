luku = int(input("Enter an integer: "))

if luku < 2:
    print(f"{luku} is not a prime number.")
else:
    on_alkuluku = True

    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"{luku} is a prime number.")
    else:
        print(f"{luku} is not a prime number.")
