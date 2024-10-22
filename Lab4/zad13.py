from random import randint

n = 7
m = 10

# a = []
# for i in range(n):
#     for j in range(m):
#     numberRandom = randint(0,20)
#     a.append([numberRandom])
# print(a)


matrix = [] * n
for i in range(n):
    numberRandom = randint(0, 20)
    for j in range(m):
        matrix[i] = numberRandom
print(matrix)