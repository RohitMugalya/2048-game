CONTROLS = """
    8
    ↑   
4 ← ◉ → 6
    ↓
    2"""
SCORE = 0


def is_game_over(matrix):
    for i in range(4):
        pre = matrix[i][0]
        for j in range(1, 4):
            suc = matrix[i][j]
            if suc == 0:
                continue
            if pre == suc:
                return False
            pre = suc

    for j in range(4):
        pre = matrix[0][j]
        for i in range(1, 4):
            suc = matrix[i][j]
            if suc == 0:
                continue
            if pre == suc:
                return False
            pre = suc

    return True


def null_coords(matrix):
    return [(i, j) for i in range(4) for j in range(4) if matrix[i][j] == 0]


def screen(lst):
    lst_with_max_ele = [max(row) for row in lst]
    high = max(lst_with_max_ele)
    n = len(str(high)) + 2
    hyphen = '-' * n
    row = f"+{hyphen}+{hyphen}+{hyphen}+{hyphen}+"
    print(row)
    for j in lst:
        print('|', end='')
        for ele in j:
            if ele == 0:
                print("|".rjust(n + 1), end='')
            else:
                print(str(ele).center(n), end='')
                print('|', end='')

        print()

    print(row)
    print(f"\nSCORE : {SCORE}")


def get_score():
    return SCORE


#   Moving Block vals
TIMES = 2


def up(arr, n=TIMES):
    for _ in range(n):  # To move upon leading 0s
        for row in range(3):
            for j in range(4):  # four vals in row
                if arr[row][j] == 0:
                    arr[row][j], arr[row + 1][j] = arr[row + 1][j], arr[row][j]


def down(arr, n=TIMES):
    for _ in range(n):  # To move upon leading 0s
        for row in range(3):
            for j in range(4):  # four vals in row
                if arr[row + 1][j] == 0:
                    arr[row][j], arr[row + 1][j] = arr[row + 1][j], arr[row][j]


def right(arr, n=TIMES):
    for _ in range(n):  # To move upon leading 0s
        for row in range(4):
            if 0 in arr[row]:  # To Decrease complexity
                for j in range(3):  # To Avoid IndexError
                    if arr[row][j + 1] == 0:
                        arr[row][j], arr[row][j + 1] = arr[row][j + 1], arr[row][j]


def left(arr, n=TIMES):
    for _ in range(n):
        for row in range(4):
            if 0 in arr[row]:
                for j in range(3):  # To Avoid IndexError
                    if arr[row][j] == 0:
                        arr[row][j], arr[row][j + 1] = arr[row][j + 1], arr[row][j]


#   evaluating twins
def eval_up_vals(arr):
    global SCORE
    up(arr)
    for row in range(3):
        for j in range(4):  # four vals in row
            if (arr[row][j] == arr[row + 1][j]) and (arr[row][j] != 0):  # To <ease complexity
                SCORE += 2 * (arr[row][j])
                arr[row][j], arr[row + 1][j] = 2 * (arr[row][j]), 0
    up(arr, 2)  # 2 To <es complexity


def eval_down_vals(arr):
    global SCORE
    down(arr)
    for row in range(3, 0, -1):  # 3,2,1 indices
        for j in range(4):
            if (arr[row][j] == arr[row - 1][j]) and (arr[row][j] != 0):  # Adding both 0s =lts same
                SCORE += 2 * (arr[row][j])
                arr[row][j], arr[row - 1][j] = 2 * (arr[row][j]), 0

    down(arr, 2)


def eval_right_vals(arr):
    global SCORE
    right(arr)
    for row in range(4):
        for j in range(3, 0, -1):  # 3,2,1 To Avoid IndexError
            if (arr[row][j] == arr[row][j - 1]) and (arr[row][j] != 0):
                SCORE += 2 * (arr[row][j])
                arr[row][j], arr[row][j - 1] = 2 * arr[row][j], 0
    right(arr, 2)


def eval_left_vals(arr):
    global SCORE
    left(arr)
    for row in range(4):
        for j in range(3):
            if (arr[row][j] == arr[row][j + 1]) and (arr[row][j] != 0):
                SCORE += 2 * (arr[row][j])
                arr[row][j], arr[row][j + 1] = 2 * (arr[row][j]), 0
    left(arr, 2)
