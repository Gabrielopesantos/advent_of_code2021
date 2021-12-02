with open("./day_2/input.txt", "r") as input:
    input = [(c.split()[0], int(c.split()[-1])) for c in input.readlines()] 


# pt1

c = [0, 0]

for action, value in input:
    if action == "up":
        c[1] -= value
    if action == "down":
        c[1] += value
    if action == "forward":
        c[0] += value

print(f"Part 1: {c[0]*c[1]}")

# pt2

c_a = [0, 0, 0]

for ac_ation, value in input:
    if ac_ation == "up":
        c_a[2] -= value
    if ac_ation == "down":
        c_a[2] += value
    if ac_ation == "forward":
        c_a[0] += value
        c_a[1] += c_a[2] * value

print(f"Part 2: {c_a[0]*c_a[1]}")
