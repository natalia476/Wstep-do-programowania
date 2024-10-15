suma = 0
for i in range(1, 40, 2):
    suma += i
print(suma)

suma2 = 0
for i in range(40):
    if i % 2 == 0:
        continue
    suma2 += i
print(suma2)
