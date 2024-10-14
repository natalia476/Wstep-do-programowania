a = 5
b = 13
c = 12

if a < b:
    if c < a:
        print("c jest najmniejsza")
    elif c == a:
        print("a i c są najmniejsze")
    else:
        print("a jest najmniejsza")
elif b < a:
    if b < c:
        print("b jest najmniejsza")
    elif b == c:
        print("b i c są najmniejsze")
    else:
        print("c jest najmniejsza")
elif c < a:
    print("c jest najmniejsza")
elif a == b:
    if b == c:
        print("Wszystkie liczby są takie same")
    else:
        print("a i b są najmniejsze")
