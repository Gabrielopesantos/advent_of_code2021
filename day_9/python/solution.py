from copy import deepcopy

with open("./day_9/input.txt", "r") as input:
    input = [list(map(int, list(line.strip()))) for line in input.readlines()]

nrows = len(input)
ncols = len(input[0])

# pt1
risk_pts = []
for r in range(nrows):
    for c in range(ncols):
        value = input[r][c]
        if value == 9:
            continue
        risk = True
        for r_, c_ in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= r+r_ < nrows and 0 <= c+c_ < ncols:
                if input[r+r_][c+c_] < input[r][c]:
                    risk = False
                    break
            else:
                continue
        if risk:
                risk_pts.append(value+1)
print("Part 1:", sum(risk_pts))
        
# pt2
basins = []
pt2_input = deepcopy(input)

for r in range(nrows):
    for c in range(ncols):
        if pt2_input[r][c] == 9:
            continue
        basin = [(r, c)]
        points_visited = {(r, c)}
        b_size = 0

        while basin:
            b_size += 1
            r, c = basin.pop()
            pt2_input[r][c] = 9

            for r_, c_ in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= r+r_ < nrows and 0 <= c+c_ < ncols:
                    n = (r+r_, c+c_)
                    if pt2_input[n[0]][n[1]] != 9 and n not in points_visited:
                        basin.append(n)
                        points_visited.add(n)
                else:
                    continue
        basins.append(b_size)
b1, b2, b3, *_ = sorted(basins, reverse=True)
print("Part 2", b1* b2* b3)