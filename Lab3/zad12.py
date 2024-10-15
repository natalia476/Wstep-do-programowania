m = [2, 6, 12, 15, 21]
min = 0
max = 0
for i in m:
    for j in m:
        if i < j:
            min = i
print(min)