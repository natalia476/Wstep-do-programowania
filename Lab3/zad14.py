x = 3562
print(x % 10)
print((x - x % 10)/10 % 10)
#to samo co wyzej tylko liczba calkowita
print((int)(x - x % 10)/10 % 10)


suma2=0
while x > 0:
    cyfra = x % 10
    suma2 += cyfra
    x = x // 10
print(suma2)