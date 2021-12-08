from collections import defaultdict

with open("./day_8/input.txt", "r") as input:
    input = [row.strip().split(" | ") for row in input.readlines()]


# pt1
n = 0
for _, digits in input:
    n += sum([1 if len(d) in [2, 4, 3, 7] else 0 for d in digits.split()])
print("Part 1: ", n)

# pt2
def reverse_dict(dct):
    return {v:k for k,v  in dct.items()}

total = 0
for ps, ds in input:
    ps = ["".join(sorted(p)) for p in ps.split()]
    ds = ["".join(sorted(d)) for d in ds.split()]
    map = defaultdict(int, {k: -1 for k in (ps)})

    # Set known values
    for d, l in zip([1, 4, 7, 8], [2, 4, 3, 7]):
        k = [k for k in map if len(k) == l][0]
        map[k] = d
    
    # 6
    opt6 = [k for k,v in map.items() if len(k) == 6 and v == -1]
    for o in opt6:
        if set(reverse_dict(map)[7]).difference(o):
            map[o] = 6

    # 5
    opt5 = [k for k,v in map.items() if len(k) == 5 and v == -1]
    for o in opt5:
        if len(set(reverse_dict(map)[6]).difference(o)) == 1:
            map[o] = 5

    # 3
    opt3 = [k for k,v in map.items() if len(k) == 5 and v == -1]
    for o in opt3:
        if len(set(reverse_dict(map)[5]).difference(o)) == 1:
            map[o] = 3

    # 0
    opt0 = [k for k,v in map.items() if len(k) == 6 and v == -1]
    for o in opt0:
        if len(set(reverse_dict(map)[4]).difference(o)) == 1:
            map[o] = 0

    # 9
    opt9 = [k for k, v in map.items() if len(k) == 6 and v == -1][0]
    map[opt9] = 9

    # 2
    opt2 = [k for k, v in map.items() if len(k) == 5 and v == -1][0]
    map[opt2] = 2

    output = int("".join([str(map[d]) for d in ds]))
    total += output

print("Part 2: ", total)