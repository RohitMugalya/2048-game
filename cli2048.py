from copy import deepcopy
import random as rr
import os

from util import eval_down_vals, eval_up_vals, eval_left_vals, eval_right_vals
from util import screen, is_game_over, CONTROLS, null_coords


board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

MOVES = 0
print(CONTROLS)

index0 = null_coords(board)                 # returns list of (i, j) ie 0
ri, rj = rr.choice(index0)
board[ri][rj] = rr.choice((2, 2, 2, 4))

screen(board)

while not is_game_over(board) or index0:

    #  Menu Driven
    previous_state = after_state = deepcopy(board)
    while previous_state == after_state:
        previous_state = deepcopy(board)
        move = input("Move:> ")
        if move == '8':
            eval_up_vals(board)
        elif move == '2':
            eval_down_vals(board)
        elif move == '6':
            eval_right_vals(board)
        elif move == '4':
            eval_left_vals(board)
        else:
            print(f"Invalid input Game Controls is:\n{CONTROLS}")
            continue
        after_state = deepcopy(board)

    MOVES += 1
    index0 = null_coords(board)  # Returns list of (i, j) ie 0
    if index0:
        ri, rj = rr.choice(index0)
        toss = rr.choice((2, 2, 2, 4))
        board[ri][rj] = toss
        index0.remove((ri, rj))

    os.system('cls')
    screen(board)


print(f"Total No.of Moves : {MOVES}")
print("Game Over!\nTry Again:(")
