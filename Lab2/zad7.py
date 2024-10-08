a = 4
b = 4

if a > 0 and b > 0:
    P = a * b
    print("Pole prostokąta wynosi: ", P)
    if a == b:
        print("Postokąt jest kwadratem!")
    else:
        print("Prostokąt nie jest kwadratem!")
else:
    print("Błędne dane")
    print("Boki prostokąta muszą być dodatnie")