bacteriaNumber = 100

for i in range(1, 11):
    bacteriaNumber = bacteriaNumber * 1.1
    print("Godzina ", i, ": ", f"{bacteriaNumber:.0f}", " bakterii", sep="")