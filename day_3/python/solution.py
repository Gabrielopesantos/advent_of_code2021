import copy

with open("./day_3/input.txt", "r") as input:
    input = [list(map(int, l.strip())) for l in input.readlines()]


# pt1

c = [0 for _ in range(len(input[0]))]

for l in input:
    for i, b in enumerate(l):
        if b == 1:
            c[i] += 1
        else:
            c[i] -= 1

gamma = []
epsi = []

for b in c:
    if b > 0:
        gamma.append("1")
        epsi.append("0")
    else:
        gamma.append("0")
        epsi.append("1")
    
gamma_str = "".join(gamma)
epsi_str = "".join(epsi)

print(f"Part 1: {int(gamma_str, 2)* int(epsi_str, 2)}")

# pt2

o2 = input.copy()
co2 = input.copy()

b_pos = 0
while len(o2) > 1:
    v = sum([l[b_pos] for l in o2])/len(o2)
    if v >= .5:
        o2 = [l for l in o2 if l[b_pos] == 1]
    else:
        o2 = [l for l in o2 if l[b_pos] == 0]
    b_pos += 1

b_pos = 0
while len(co2) > 1:
    v = sum([l[b_pos] for l in co2])/len(co2)
    if v >= .5:
        co2 = [l for l in co2 if l[b_pos] == 0]
    else:
        co2 = [l for l in co2 if l[b_pos] == 1]
    b_pos += 1

o2_val = int("".join(map(str, o2[0])), 2)
co2_val = int("".join(map(str, co2[0])), 2)

print(f"Part 2: {o2_val*co2_val}")