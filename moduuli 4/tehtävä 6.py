import random
N = int(input())
count_inside = 0
i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        count_inside += 1
    i += 1
pi_approx = 4 * count_inside / N
print(f"Approximation of pi: {pi_approx:.4f}")