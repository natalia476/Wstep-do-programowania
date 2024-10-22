print("Podaj boki prostokąta a i b:")
numbers = input()
numberList = numbers.split()
integerList = list(map(int, numberList))

if integerList[0] > 0 and integerList[1] > 0:
    area = integerList[0] * integerList[1]
    circuit = 2 * integerList[0] + 2 * integerList[1]
else:
    print("Podaj dodatnią liczbę")
print(f"Pole prostokąta P= {area}, a obwód L={circuit}")