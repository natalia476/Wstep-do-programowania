print("Podaj bok trojkata:")
number = int(input())

for i in range(number + 1):
    print(((number - i) * " ") + (i * "X"))