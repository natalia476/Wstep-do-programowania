import math

numberOfPars = 0
listOfPrimes = []

for i in range(2, 101):
    isPrime = True
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            isPrime = False
            break
        elif i == j:
            break
        else:
            isPrime = True
            j += 1
    if isPrime:
        listOfPrimes.append(i)

for i in listOfPrimes:
    for j in listOfPrimes:
        if j - i == 2:
            print(i, j)
            numberOfPars += 1

print("Liczba par bliźniaczych:", numberOfPars)

