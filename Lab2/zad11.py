a = 7
b = 9
c = 4

if a == b and b == c:
    print("Wszystkie liczby a, b, c są sobie równe")
elif a == b and a != c:
    print("Liczby a i b są równe")
elif b == c:
    print("Liczby b i c są równe")
elif a == c:
    print("Liczby a i c są równe")
else:
    print("Nie ma pary równych liczb")