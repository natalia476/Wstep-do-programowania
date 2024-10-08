a = 5
b = 5
c = 10

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
else:
    print("a i b są najmnijsze")