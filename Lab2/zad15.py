a = 3
b = 4
c = 5

if a < (b + c) and b < (a + c) and c < (a +b):
    if a == b == c:
        print("Trójkąt równoboczny")
        boki = sorted([a, b, c])
        a, b, c = boki[0], boki[1], boki[2]
        if a ** 2 + b ** 2 == c ** 2:
            print("Trójkąt prostokątny")
        elif a ** 2 + b ** 2 > c ** 2:
            print("Trójkąt ostrokątny")
        else:
            print("Trójkąt rozwartokątny")
    elif a != b and b != c:
        print("Trójkąt różnoboczny")
        boki = sorted([a, b, c])
        a, b, c = boki[0], boki[1], boki[2]
        if a ** 2 + b ** 2 == c ** 2:
            print("Trójkąt prostokątny")
        elif a ** 2 + b ** 2 > c ** 2:
            print("Trójkąt ostrokątny")
        else:
            print("Trójkąt rozwartokątny")
    elif a == b or b == c or a == c:
        boki = sorted([a, b, c])
        a, b, c = boki[0], boki[1], boki[2]
        print("Trójkąt równoramienny")
        if a ** 2 + b ** 2 == c ** 2:
            print("Trójkąt prostokątny")
        elif a ** 2 + b ** 2 > c ** 2:
            print("Trójkąt ostrokątny")
        else:
            print("Trójkąt rozwartokątny")
else:
    print("To nie są boki trójkąta.")
