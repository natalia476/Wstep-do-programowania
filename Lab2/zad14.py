import math

a = 0
b = 1
c = 1

delta = (b)**2 - 4*a*c
if a == 0:
    if b == 0:
        print('Równanie tożsamościowe')
    else:
        print('Równanie sprzeczne')
else:
    x = -b / a

if delta > 0:
    x1 = (-b - math.sqrt(delta) / (2 * a))
    x2 = (-b + math.sqrt(delta) / (2 * a))
    print(x1, x2)
elif delta == 0:
    x3 = -b * (2 * a)
    print(x3)
else:
    print("Brak rozwiązań")


if a == 0:
    if b == 0:
        if c == 0:
            print("Nieskończenie wiele rozwiązań")
        elif c > 0:
            print("Brak rozwiązań")
    elif b > 0:
        if c > 0:
            print("Jedno rozwiązanie:", x3)
elif a > 0:
    if b == 0:
        if c < 0:
            print("Dwa rozwiązania", x1, "i", x2)
        elif c > 0:
            print("Brak rozwiązania")
    elif b < 0:
        if c > 1:
            print("Jedno rozwiązanie", x3)
    elif b > 0:
        if c > 0:
            print("Dwa rozwiązania", x1, "i", x2)

