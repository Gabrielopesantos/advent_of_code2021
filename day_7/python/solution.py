import statistics

with open("./day_7/input.txt", "r") as input:
    crabs = list(map(int, input.read().split(",")))

# pt1
p = int(statistics.median(crabs))
fuel = sum([abs(p-c) for c in crabs])
print("Part 1: ", fuel)

# pt2
fuels = []
for p in range(min(crabs), max(crabs)):
    fuels.append(int(sum([(abs(c-p)*(1+abs(c-p))/2) for c in crabs])))

print("Part 2: ", min(fuels))