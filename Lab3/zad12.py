m = [2, 6, 12, 15, 21]
min = 100
max = 0

for i in m:
    if i > max:
        max = i

for i in m:
    if i < min:
        min = i

print(max)
print(min)