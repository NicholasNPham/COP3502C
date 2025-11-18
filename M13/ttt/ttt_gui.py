import pygame, sys
from constants import *
from tictactoe import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize Fonts to Draw X and O
chip_font = pygame.font.Font(None, CHIP_FONT)

# Initialize a Board
board = initialize_board()
# board[1][1] = "x"
# board[2][1] = "o"
# board[1][2] = "x"
player = 1
chip = "x"
game_over = False
winner = 0

def draw_grids():
    # Draw Horizontal Lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    # Draw Vertical Lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_chips():
    chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
    chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)

    for row in range(BOARD_ROWS):
        for cols in range(BOARD_COLS):
            if board[row][cols] == "x":
                chip_x_rect = chip_x_surf.get_rect(center = (cols * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2))
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][cols] == "o":
                chip_o_rect = chip_o_surf.get_rect(center = (cols * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2))
                screen.blit(chip_o_surf, chip_o_rect)

screen.fill(pygame.Color(BG_COLOR))
draw_grids()
draw_chips()

while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y) # STOPPED at 19:25

    pygame.display.update()