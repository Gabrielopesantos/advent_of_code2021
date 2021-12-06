from copy import copy

with open("./day_6/input.txt", "r") as input:
    input = list(map(int,input.read().split(",")))

def get_counter(lst):
    return {v: lst.count(v) for v in sorted(set(lst))}

## pt1
day = 0
f_day = copy(get_counter(input))
while day != 80:
    tmp_f_day = {}

    for d, n in f_day.items():
        if d == 0:
            tmp_f_day[6] = n
            tmp_f_day[8] = n
        else:
            if d-1 in tmp_f_day:
                tmp_f_day[d-1] = tmp_f_day[d-1] + n
            else:
                tmp_f_day[d-1] = n
    f_day = copy({k: tmp_f_day[k] for k in sorted(tmp_f_day)})
    day+=1

print("Part 1:", sum(v for v in f_day.values()))

## pt2
day = 0
f_day = copy(get_counter(input))
while day != 256:
    tmp_f_day = {}

    for d, n in f_day.items():
        if d == 0:
            tmp_f_day[6] = n
            tmp_f_day[8] = n
        else:
            if d-1 in tmp_f_day:
                tmp_f_day[d-1] = tmp_f_day[d-1] + n
            else:
                tmp_f_day[d-1] = n
    f_day = copy({k: tmp_f_day[k] for k in sorted(tmp_f_day)})
    day+=1

print("Part 2:", sum(v for v in f_day.values()))