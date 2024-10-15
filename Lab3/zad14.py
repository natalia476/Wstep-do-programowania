x = 3562
print(x % 10)
print((x - x % 10)/10 % 10)
#to samo co wyzej tylko liczba calkowita
print((int)(x - x % 10)/10 % 10)

cyfraJednosci = x % 10
cyfraDziesiatek = (x // 10) % 10
cyfraSetek = (x // 100) % 10
cyfraTysiecy = (x // 1000) % 10
suma = cyfraJednosci + cyfraDziesiatek + cyfraSetek + cyfraTysiecy
print(suma)