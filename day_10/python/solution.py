from collections import deque

with open("./day_10/input.txt", "r") as input:
    input = [line.strip() for line in input.readlines()]


open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]

# pt1

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

corrupted = []
rm_from_pt2 = []
for i, l in enumerate(input):
    stack = deque()
    for c in l:
        if c in open:
            stack.appendleft(c)
        else:  # c has to be in "close"
            if any([True if c == close[i] and stack[0] == open[i] else False for i in range(4)]):
                stack.popleft()
            else:
                corrupted.append(c)
                rm_from_pt2.append(i)
                break

print(sum(points[c] for c in corrupted))

# pt2

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

pt2_input = [l for i, l in enumerate(input) if i not in rm_from_pt2]

stacks = []
for i, l in enumerate(pt2_input):
    stack = deque()
    for c in l:
        if c in open:
            stack.appendleft(c)
        else:  # c has to be in "close"
            if any([True if c == close[i] and stack[0] == open[i] else False for i in range(4)]):
                stack.popleft()
    stacks.append(list(stack))

pts_line = []
for l in stacks:
    score = 0
    for c in l:
        score *= 5
        score += points[close[open.index(c)]]
    pts_line.append(score)

pts_line.sort()
print(pts_line[len(pts_line)//2])