import copy
from collections import Counter

with open("./day_4/input.txt", "r") as input:
    drawn = list(map(int,input.readline().split(",")))

    boards = [list(map(int, s.strip().replace("\n", " ").replace("  ", " ").split(" "))) for s  in input.read().split("\n\n")]

# pt1 and pt2

def mark_check_if_wins(number, board):
    won = False
    if number in board:
        board[board.index(number)] = -1

        rows_filled = []
        cols_filled = []

        for i, n in enumerate(board):
            if n == -1:
                rows_filled.append(i % 5)
                cols_filled.append(int(i / 5))

        if 5 in Counter(rows_filled).values() or 5 in Counter(cols_filled).values():
            won = True

    return won 

won = []
for i_d, n_drawn in enumerate(drawn):
    won_this_round = []
    for i_b, b in enumerate(boards):
        if mark_check_if_wins(n_drawn, b):
            unmarked = sum([n for n in b if n != -1])
            won_this_round.append((i_b, unmarked*n_drawn, b))

    if won_this_round:
        winners = [(w[0], w[1]) for w in won_this_round]
        for w  in winners:
            if w[0] not in [w[0] for w in won]:
                won.append(w)

print(f"Part 1: {won[0][1]}")
print(f"Part 2: {won[-1][1]}")