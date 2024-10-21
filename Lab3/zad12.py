m = [2, 6, 12, 15, 1]
min = m[0]
max = m[0]

for i in m:
    if i > max:
        max = i
    if i < min:
        min = i

print(min)
print(max)