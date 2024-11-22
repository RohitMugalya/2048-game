import random as rr
import sys
from copy import deepcopy

import pygame

from util import get_score, eval_up_vals, eval_down_vals, eval_left_vals, eval_right_vals, null_coords, is_game_over


GEOMETRY = WIDTH, HEIGHT = 400, 500
pygame.init()
screen = pygame.display.set_mode(GEOMETRY)
pygame.display.set_caption("2048 :)")

SCORE_BOARD_COORDINATES = (200, 50)
BOX_SIZE = 90
GAP = 8
NUMBER_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (165, 42, 42)
TILE_COLOR = {
    0: (67, 53, 39),
    2: (135, 206, 235),     # Sky Blue
    4: (0, 255, 0),         # Lime
    8: (255, 165, 0),       # Orange
    16: (255, 255, 0),      # Yellow
    32: (128, 0, 128),      # Purple
    64: (0, 0, 255),        # Blue
    128: (192, 192, 192),   # Silver
    256: (0, 128, 128),     # Teal
    512: (0, 128, 0),       # Half-Green
    1024: (0, 0, 128),      # Navy
    2048: (0, 0, 0),        # Black
}
board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
MOVES = 0

X = 7
Y = 105


def refresh_screen():
    screen.fill(BACKGROUND_COLOR)
    score_font = pygame.font.Font(None, 48)
    the_score = score_font.render(f"SCORE: {get_score()}", True, (255, 255, 255))
    score_board = the_score.get_rect(center=SCORE_BOARD_COORDINATES)
    screen.blit(the_score, score_board)
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            row, col = i * (BOX_SIZE + GAP) + Y, j * (BOX_SIZE + GAP) + X
            pygame.draw.rect(screen, TILE_COLOR.get(value),
                             rect=(col, row, BOX_SIZE, BOX_SIZE))

            font = pygame.font.Font(None, 36)  # Font Size
            number = font.render(str(value if value else ''), True, (0, 0, 0))
            number_plate = number.get_rect(center=(col + BOX_SIZE // 2, row + BOX_SIZE // 2))
            screen.blit(number, number_plate)

    pygame.display.update()


index0 = null_coords(board)         # returns list of (i, j) ie 0
ri, rj = rr.choice(index0)
board[ri][rj] = rr.choice((2, 2, 2, 4))

while not is_game_over(board) or index0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYUP:
            previous_state = deepcopy(board)
            match event.key:
                case pygame.K_UP:
                    eval_up_vals(board)
                case pygame.K_DOWN:
                    eval_down_vals(board)
                case pygame.K_RIGHT:
                    eval_right_vals(board)
                case pygame.K_LEFT:
                    eval_left_vals(board)

            after_state = deepcopy(board)

            if previous_state != after_state:
                MOVES += 1
                index0 = null_coords(board)     # returns list of (i, j) ie 0
                ri, rj = rr.choice(index0)
                board[ri][rj] = rr.choice((2, 2, 2, 4))
                index0.remove((ri, rj))
                print(f"{MOVES = }")
                print(*board, sep='\n', end='\n\n')
        refresh_screen()


RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    refresh_screen()
    game_over_font = pygame.font.Font(None, 65)
    game_over = game_over_font.render("GAME OVER : (", True, (168, 0, 0))
    game_over_board = game_over.get_rect(center=(200, 250))
    screen.blit(game_over, game_over_board)

    pygame.display.update()
