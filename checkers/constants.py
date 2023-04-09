import pygame

WIDTH = 800
HEIGHT = 800

# 8 BY 8 BOARD WHICH IS THE STANDARD SIZE
ROWS = 8
COLS = 8

# SIZE OF EACH CELL ON THE BOARD
CELL_SIZE = WIDTH // COLS

# RGB COLOR CODING
RED = (204, 0, 0)
DARKRED = (153, 0, 0)
DARKGREY = (64, 64, 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BROWN = (139, 69, 19)
BEIGE = (245, 245, 220)

# LOAD KING CROWN
CROWN = pygame.transform.scale(pygame.image.load('checkers/icons/king.png'), (45, 25))
