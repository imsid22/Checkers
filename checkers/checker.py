from dataclasses import dataclass
from typing import Tuple
from .constants import RED, WHITE, GREY, CELL_SIZE
import pygame

@dataclass
class Checker:
    color: Tuple[int, int, int]
    row: int
    col: int
    padding: int = 10
    border: int = 2
    isKing: bool = False

    def __post_init__(self):
        if self.color == RED:
            self.direction = -1
        elif self.color == WHITE:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = CELL_SIZE * self.col + CELL_SIZE // 2
        self.y = CELL_SIZE * self.row + CELL_SIZE // 2

    def set_king(self):
        self.isKing = True

    def draw(self, window):
        radius = CELL_SIZE // 2 - self.padding
        # Padding for the checker inside a cell
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + self.border)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

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
