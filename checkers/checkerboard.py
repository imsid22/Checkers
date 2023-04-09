import pygame

from dataclasses import dataclass
from typing import List
from .constants import BLACK, RED, BROWN, BEIGE, ROWS, COLS, CELL_SIZE
from .checker import Checker

@dataclass
class CheckerBoard:
    board: List[List] = None
    selected_checker = None # Need to come back here
    red_remain: int = 12
    black_remain: int = 12
    red_kings: int = 0
    black_kings: int = 0

    def __post_init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        for row in range(ROWS):
            for col in range(COLS):
                if col % 2 == (row+1) % 2:
                    if row < 3:
                        self.board[row][col] = Checker(BLACK, row, col)
                    elif row > 4:
                        self.board[row][col] = Checker(RED, row, col)

    def draw_cells(self, window):
        window.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, BEIGE, (row*CELL_SIZE, col*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw(self, window):
        self.draw_cells(window)
        for row in range(ROWS):
            for col in range(COLS):
                checker = self.board[row][col]
                if checker != 0:
                    checker.draw(window, checker.color)

    def move(self, checker, row, col):
        self.board[checker.row][checker.col], self.board[row][col] = self.board[row][col], self.board[checker.row][checker.col]
        checker.move(row, col)

        if row == ROWS-1 or row == 0:
            checker.set_king()
            if checker.color == BLACK:
                self.black_kings += 1
            elif checker.color == RED:
                self.red_kings += 1

    def get_checker(self, row, col):
        return self.board[row][col]

    # def print_board(self):
    #     printing_board = [['' for _ in range(self.n)] for _ in range(self.n)]
    #     for row in range(self.n):
    #         for col in range(self.n):
    #             if self.board[row][col] != '':
    #                 printing_board[row][col] = self.board[row][col].get_color
    #
    #     for row in printing_board:
    #         print(row)
    #
    # def get_valid_moves(self):
    #     pass
    #
    # def valid_move(self, source, destination):
    #     # current_position = checker.get_position
    #     if self.board[source[0]][source[1]] == "":
    #         return False
    #     if abs(destination[0] - source[0]) > 2 or\
    #         abs(destination[1] - source[1]) > 2:
    #         return False
    #     if abs(destination[0] - source[0]) != abs(destination[1] - source[1]):
    #         return False
    #     if destination[0] < 0 or destination[0] >= self.n or destination[1] < 0 or destination[1] >= self.n:
    #         return False
    #     if self.board[destination[0]][destination[1]] != "":
    #         return False
    #     return True
    #
    # def move_checker(self, source, destination):
    #     if abs(destination[0]-source[0]) == 2 and \
    #             abs(destination[1] - source[1]) == 2:
    #         if self.check_capture(source, destination):
    #             if self.board[self.capture_x][self.capture_y].get_color == "W":
    #                 self.whites_remain -= 1
    #             else:
    #                 self.blacks_remain -= 1
    #             self.board[self.capture_x][self.capture_y].set_captured(True)
    #             self.board[self.capture_x][self.capture_y] = ""
    #
    #     self.board[source[0]][source[1]].set_position(destination)
    #     self.board[destination[0]][destination[1]] = self.board[source[0]][source[1]]
    #     self.board[source[0]][source[1]] = ""
    #
    # def check_capture(self, source, destination):
    #     if destination[0] > source[0]:
    #         self.capture_x = destination[0] - 1
    #     else:
    #         self.capture_x = destination[0] + 1
    #     if destination[1] > source[1]:
    #         self.capture_y = destination[1] - 1
    #     else:
    #         self.capture_y = destination[1] + 1
    #
    #     if self.board[self.capture_x][self.capture_y] != "":
    #         return True
    #     else:
    #         return False
    #
    # def check_end_game(self):
    #     if self.whites_remain == 0:
    #         print('Black Wins')
    #     elif self.blacks_remain == 0:
    #         print('White Wins')
    #
    # def simulate_move(self, source, destination):
    #     if self.valid_move(source, destination):
    #         self.check_end_game()
    #         self.move_checker(source, destination)
