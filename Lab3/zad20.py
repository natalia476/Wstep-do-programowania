time = [0, 2, 4, 6, 8]
distance = [0, 10, 20, 40, 60]

for i in range(1, len(time)):
    timeDelta = time[i] - time[i - 1]
    distanceDelta = distance[i] - distance[i - 1]
    velocity = distanceDelta / timeDelta
    print("Prędkośc na odcinku: ", time[i-1], "s-", time[i], "s ", velocity, sep="")

timeTotal = time[-1] - time[0]
distanceTotal = distance[-1] - distance[0]
velocityAverage = distanceTotal / timeTotal
print("Średnia prędkość na całym dystansie to", velocityAverage)
