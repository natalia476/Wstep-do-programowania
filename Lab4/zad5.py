print("Podaj imiona odzielone przecinkami:")
names = input()
namesList = names.split(",")
girlsNames= []
for name in namesList:
    if name.endswith("a"):
        girlsNames.append(name)

print(girlsNames)
