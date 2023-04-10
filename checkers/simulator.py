import pygame
from dataclasses import dataclass
from .constants import RED, BLACK, BLUE, CELL_SIZE
from .checkerboard import CheckerBoard
from typing import Tuple, Dict, Union


@dataclass
class Simulator:
    window: Union
    selected = None  # Unsure about the datatype
    board: CheckerBoard = None
    possible_moves: Dict = None
    player: Tuple[int, int, int] = None

    def __post_init__(self):
        self._init()

    def update(self):
        self.board.draw(self.window)
        self.draw_possible_moves(self.possible_moves)
        pygame.display.update()

    def _init(self):
        self.possible_moves = {}
        self.board = CheckerBoard()
        self.player = RED
        self.selected = None

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            # If move is invalid
            if not result:
                self.selected = None
                self.select(row, col)

        checker = self.board.get_checker(row, col)
        # Clicking on a checker whose turn it is
        if checker and checker.color == self.player:
            self.selected = checker
            self.possible_moves = self.board.get_possible_moves(checker)
            return True

        return False

    def _move(self, row, col):
        checker = self.board.get_checker(row, col)
        if self.selected and checker == 0 and (row, col) in self.possible_moves:
            self.board.move(self.selected, row, col)
            jumped = self.possible_moves[(row, col)]
            if len(jumped) > 0:
                self.board.remove(jumped)
            self.switch_player()
        else:
            return False
        return True

    def draw_possible_moves(self, moves):
        for move in moves.keys():
            row, col = move
            pygame.draw.circle(self.window, BLUE, (col * CELL_SIZE + CELL_SIZE//2, row * CELL_SIZE + CELL_SIZE//2), 15) # radius

    def switch_player(self):
        self.possible_moves = {}
        if self.player == RED:
            self.player = BLACK
        elif self.player == BLACK:
            self.player = RED


