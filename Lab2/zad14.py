import math

a = 1
b = 5
c = 6

delta = (b) ** 2 - 4 * a * c

if a == 0:
    if b == 0:
        if c == 0:
            print("Nieskończenie wiele rozwiązań")
        elif c != 0:
            print("Brak rozwiązań")
    else:
        x = -c / b
        print("Jedno rozwiązanie:", x)
else:
    if b == 0:
        if c > 0:
            print("Brak rozwiązań")
        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print("Dwa rozwiązania", x1, "i", x2)
    elif b < 0:
        x1 = (-b - math.sqrt(delta) / (2 * a))
        print("Jedno rozwiązanie podwójne", x1)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Dwa rozwiązania", x1, "i", x2)

# else:
#     if delta > 0:
#         x1 = (-b - math.sqrt(delta)) / (2 * a)
#         x2 = (-b + math.sqrt(delta)) / (2 * a)
#         print("Dwa rozwiązania", x1, "i", x2)
#     elif delta == 0:
#         x = -b * 2 * a
#         print("Jedno rozwiązanie", x)
#     else:
#         print("Brak rozwiązania")
