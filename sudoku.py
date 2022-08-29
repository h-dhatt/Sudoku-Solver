from random import sample


def generate_board(num):
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    board_tmp = [[nums[pattern(r, c)] for c in cols] for r in rows]

    print("=======full board========")
    print_board(board_tmp)

    squares = side * side
    if num == 0:
        empties = squares * 3 // 4
    else:
        empties = 81 - num
    for p in sample(range(squares), empties):
        board_tmp[p // side][p % side] = 0

    return board_tmp



def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    print("")


def possible(bo, pos, num):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):  # row
        for j in range(box_x * 3, box_x * 3 + 3):  # col
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def next_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  


def solve(bo):
    slot = next_empty(bo)
    if not slot:
        return True
    else:
        row, col = slot
    for i in range(1, 10):
        if possible(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


board = [
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],

    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],

    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 0]
]

board = generate_board(0)


print("======solvable board=====")
print_board(board)

solve(board)

print("======solved board=======")
print_board(board)
