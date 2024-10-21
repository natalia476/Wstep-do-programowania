import math

numberOfTriples = 0

for a in range(2, 51):
    for b in range(a + 1, 51):
        c = math.sqrt(a ** 2 + b ** 2)
        if c.is_integer() and c <= 50:
            numberOfTriples += 1
print(numberOfTriples)