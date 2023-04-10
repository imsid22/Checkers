from dataclasses import dataclass
from typing import Tuple
from .constants import RED, BLACK, DARKRED, DARKGREY, CELL_SIZE, CROWN
import pygame

@dataclass
class Checker:
    color: Tuple[int, int, int]
    row: int
    col: int
    padding: int = 15
    border: int = 1
    isKing: bool = False
    direction: int = None
    x: int = None
    y: int = None

    def __post_init__(self):
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = CELL_SIZE * self.col + CELL_SIZE // 2
        self.y = CELL_SIZE * self.row + CELL_SIZE // 2

    def set_king(self):
        self.isKing = True

    @property
    def get_king(self):
        return self.isKing

    def draw(self, window, color):
        radius = CELL_SIZE // 2 - self.padding
        # Padding for the checker inside a cell
        if color == BLACK:
            pygame.draw.circle(window, DARKGREY, (self.x, self.y), radius + self.border)
            pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        elif color == RED:
            pygame.draw.circle(window, DARKRED, (self.x, self.y), radius + self.border)
            pygame.draw.circle(window, self.color, (self.x, self.y), radius)

        if self.isKing:
            # blit means to add an image to the screen
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()


    # representation of our object
    def __repr__(self):
        return str(self.color)








    # @property
    # def get_color(self):
    #     return self.color
    #
    # @property
    # def get_position(self):
    #     return self.position
    #
    # def set_position(self, new_position):
    #     self.position = new_position
    #
    # @property
    # def is_captured(self):
    #     return self.captured
    #
    # def set_captured(self, if_captured):
    #     self.captured = if_captured
    #
    # @property
    # def is_king(self):
    #     return self.isKing
