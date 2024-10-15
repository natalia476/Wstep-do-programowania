m = [3, -5, 2, 10, -14, 6, 8, 15, 9, 21]
suma = 0
for i in m:
    if i > 0 and i < 10:
        print(i)
        suma += i
    else:
        continue
print(suma)