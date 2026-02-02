names = set()

while True:
    name = input()

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("OK")
for n in names:
    print(n)
