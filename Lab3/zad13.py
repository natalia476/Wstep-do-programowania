x = 5

for i in range(2, x, 1):
    if x % i == 0:
        print("x nie jest liczba pierwszą")
        break
    else:
        print("x jest liczbą pierwszą")