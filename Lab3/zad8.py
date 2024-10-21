suma = 0
for i in range(0, 41, 2):
    suma += i
print(suma)

suma2 = 0
for i in range(41):
    if i % 2 == 0:
        suma2 += i
print(suma2)
