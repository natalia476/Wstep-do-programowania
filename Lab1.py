# zad1
print("Hello world")
print(" ")

#zad2
print("    ^")
print("   ^^^")
print("  ^^^^^")
print(" ^^^^^^^")
print("  ^^^^^")
print(" ^^^^^^^")
print("^^^^^^^^^")
print("   ###")
print(" ")

#zad3
x=7
print(x)
print(" ")

#zad4
a=7
b=5
print(a)
print(a+3)
print(a*3)
print(a+b)
print(a/b)
print("Suma a i b to: ", a+b)
print("a=", a, ", b=", b)
c = b-a
print(c)
print(" ")

#zad5
a=2
b=3
c=a*a
d=b*b
e=c+d
print("Liczba a = ", a, "; liczba b =", b)
print("Suma kwadratów tych liczb to ", e)
print(" ")

#zad6
a=4
h=2
p=(a*h)/2
print(p)
print(" ")

#zad7
a=2
b=3
p=a*b
obw=(2*a)+(2*b)
print(p)
print(obw)
print(" ")

#zad8
znaki = "abc hej!"
print("Znaki to:", znaki)
print(" ")

#zad9
a=3
print("Gdy do", a, "dodasz 1, to wyjdzie", a+1)
print("Gdy do", a, "dodasz 1, to wyjdzie", a+1, sep="")
print("Gdy do", a, "dodasz 1, to wyjdzie", a+1, sep="-")
print(" ")

#zad10
bombka = "o"
print("    ^")
print("   ^^^")
print("  ^",bombka,"^^^", sep="")
print(" ^^^^^",bombka,"^", sep="")
print("  ^^^^^")
print(" ^^",bombka,"^^^^", sep="")
print("^^^^^^", bombka,"^^", sep="")
print("   ###")
print(" ")

#zad11
import math
a = 16
b = math.sqrt(a)
print(b)

print(math.pi)
print(math.sin(0))
print(math.sin(math.pi/2))
print(math.floor(2.3))
print(" ")

#zad12
a=2
pole=a*a
obwod=4*a
przekatna=math.sqrt(2)*a
print(pole)
print(obwod)
print(przekatna)
print(" ")

#zad13
a = 180
b = math.radians(a)
print(b)

d=1
c = math.degrees(d)
print(c)
print(" ")

#zad14
a=4
b=3
alfa=30
pole=(a*b*math.sin(math.radians(alfa)))/2
print(pole)
print(" ")

#zad15
x_a=0
y_a=0
x_b=3
y_b=4
odleglosc=math.sqrt((x_b-x_a)**2 + (y_b-y_a)**2)
print(odleglosc)