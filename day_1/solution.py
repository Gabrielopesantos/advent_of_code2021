with open("./input.txt", "r") as input:
    input_int = list(map(int, input.readlines()))

# pt1

t_increases = sum([1 if input_int[i-1] < input_int[i] else 0 for i in range(len(input_int))])

print(f"Part 1: {t_increases}")

# pt2

sliding = [input_int[i-1] + input_int[i] + input_int[i+1] for i in range(len(input_int)-1)]
t_increases_s = sum([1 if sliding[i-1] < sliding[i] else 0 for i in range(len(sliding))])

print(f"Part 2: {t_increases_s}")