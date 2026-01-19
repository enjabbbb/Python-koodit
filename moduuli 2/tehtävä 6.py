import random
koodi_3 = [random.randint(0, 9) for _ in range(3)]
koodi_4 = [random.randint(1, 6) for _ in range(4)]
print("3-numeroinen koodi (0–9):", "".join(map(str, koodi_3)))
print("4-numeroinen koodi (1–6):", "".join(map(str, koodi_4)))