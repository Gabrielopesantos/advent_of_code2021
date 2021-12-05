from itertools import product

with open("./day_5/input.txt", "r") as input:
    input = [(list(map(int,line.split(" -> ")[0].strip().split(","))), list(map(int,line.split(" -> ")[1].strip().split(","))))
    for line in input.readlines()]

# x1, y1 = x2, y2
max_x = max([m for v in [[v[0][0], v[1][0]] for v in input] for m in v])+1
max_y = max([m for v in [[v[0][1], v[1][1]] for v in input] for m in v])+1

# pt1
def get_intermediate_points(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2

    if x1 == x2 or y1 == y2:
        if x1 == x2:
            xs = [x1]
            step = 1
            if y1 > y2:
                y2 -= 1
                step = -1
            else:
                y2 += 1
            ys = list(range(y1, y2, step)) 
        elif y1 == y2:
            ys = [y1]
            step = 1
            if x1 > x2:
                x2 -= 1
                step = -1
            else:
                x2 += 1
            xs = list(range(x1, x2, step)) 
        points = list(product(xs, ys))
    else:
        points = []

    return points

def get_diagonal_points(pt1, pt2):
    x1, y1, = pt1
    x2, y2 = pt2

    step = 1
    if x1 > x2:
        x2 -= 1
        step = -1
    else:
        x2 += 1
    xs = list(range(x1, x2, step))
    
    step = 1
    if y1 > y2:
        y2 -= 1
        step = -1
    else:
        y2 += 1
    
    ys = list(range(y1, y2, step))
    ys = [y for y in ys if y >= 0]
    xs = [x for x in xs if x >= 0]

    return list(zip(xs, ys))
    
diag_list = [0 for _ in range(max_x*max_y)]
diag = [[0] * max_y for _ in range(max_x)]

for (x1, y1), (x2, y2) in input:

    if x1 != x2 and y1 != y2:
        points = get_diagonal_points((x1, y1), (x2, y2))
        for (x, y) in points:
            diag[y][x] += 1
    else:
        points = get_intermediate_points((x1, y1), (x2, y2))
        for (x, y) in points:
            p_index = (x*(max_y)) + (y % max_y)
            diag_list[p_index] += 1
            diag[y][x] += 1


print("Part 1: ",sum([1 if p >= 2 else 0 for p in diag_list]))
print("Part 2:", sum(1 if v >= 2 else 0 for line in diag for v in line))