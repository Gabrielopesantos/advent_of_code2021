with open("./day_9/input.txt", "r") as input:
    input = [[100] + list(map(int, list(line.strip()))) + [100] for line in input.readlines()]

input.insert(0, [100]*len(input[0]))
input.append([100]*len(input[0]))

# pt1
risk_pts = []
for i in range(1, 101):
    for j in range(1, 101):
        point = input[j][i]
        if point < input[j-1][i] and point < input[j+1][i] and point < input[j][i-1] and point < input[j][i+1]:
            risk_pts.append(point+1)
print(sum(risk_pts))
        
# pt2
basins = []