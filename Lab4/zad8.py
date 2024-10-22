print("Podaj wysokosc i szerokosc prostokata:")
height = int(input())
width = int(input())

for i in range(height):
    for j in range(width + 1):
        j = j * "X"
    print(j)