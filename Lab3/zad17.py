import math

iloscLiczbPierwszych = 0

for i in range(2, 101):
    isPrime = True
    n = math.sqrt(i)
    for j in range(2, int(n + 1)):
        if i % j == 0:
            isPrime = False
            break
        elif i == j:
            break
        else:
            isPrime = True
            j += 1
    if isPrime:
        iloscLiczbPierwszych += 1

print(iloscLiczbPierwszych)