import pygame

from dataclasses import dataclass
from typing import List, Union
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

    def get_possible_moves(self, checker: Union):
        moves = {}
        if checker.color == RED:
            up = checker.row - 1
            right = checker.col + 1
            left = checker.col - 1
            if checker.get_king:
                down = checker.row + 1
                # Can we go down-left
                if self.board[down][left] != 0:
                    further_down = down + 1
                    further_left = left - 1
                    if further_down <= 7 and further_left >= 0 and not self.board[further_down][further_left]:
                        moves[(further_down, further_left)] = [(down, left)]
                else:
                    if down <= 7 and left >= 0:
                        moves[(down, left)] = []

                # Can we go down-right
                if self.board[down][right] != 0:
                    further_down = down + 1
                    further_right = right + 1
                    if further_down <= 7 and further_right <= 7 and not self.board[further_down][further_right]:
                        moves[(further_down, further_right)] = [(down, right)]
                else:
                    if down <= 7 and right <= 7:
                        moves[(down, right)] = []

                # Can we go up-left
                if self.board[up][left] != 0:
                    further_up = up - 1
                    further_left = left - 1
                    if further_up >= 0 and further_left >= 0 and not self.board[further_up][further_left]:
                        moves[(further_up, further_left)] = [(up, left)]
                else:
                    if up >= 0 and left >= 0:
                        moves[(up, left)] = []

                # Can we go up-right
                if self.board[up][right] != 0:
                    further_up = up - 1
                    further_right = right + 1
                    if further_up >= 0 and further_right <= 7 and not self.board[further_up][further_right]:
                        moves[(further_up, further_right)] = [(up, right)]
                else:
                    if up >= 0 and right <= 7:
                        moves[(up, right)] = []

            else:
                # Can we go up-left
                if self.board[up][left] != 0:
                    further_up = up - 1
                    further_left = left - 1
                    if further_up >= 0 and further_left >= 0 and not self.board[further_up][further_left]:
                        moves[(further_up, further_left)] = [(up, left)]
                else:
                    if up >= 0 and left >= 0:
                        moves[(up, left)] = []

                # Can we go up-right
                if self.board[up][right] != 0:
                    further_up = up - 1
                    further_right = right + 1
                    if further_up >= 0 and further_right <= 7 and not self.board[further_up][further_right]:
                        moves[(further_up, further_right)] = [(up, right)]
                else:
                    if up >= 0 and right <= 7:
                        moves[(up, right)] = []

        elif checker.color == BLACK:
            up = checker.row + 1
            right = checker.col - 1
            left = checker.col + 1
            if checker.get_king:
                down = checker.row - 1
                # Can we go down-left
                if self.board[down][left] != 0:
                    further_down = down - 1
                    further_left = left + 1
                    if further_down >= 0 and further_left <= 7 and not self.board[further_down][further_left]:
                        moves[(further_down, further_left)] = [(down, left)]
                else:
                    if down >= 0 and left <= 7:
                        moves[(down, left)] = []

                # Can we go down-right
                if self.board[down][right] != 0:
                    further_down = down - 1
                    further_right = right - 1
                    if further_down >= 0 and further_right >= 0 and not self.board[further_down][further_right]:
                        moves[(further_down, further_right)] = [(down, right)]
                else:
                    if down >= 0 and right >= 0:
                        moves[(down, right)] = []

                # Can we go up-left
                if self.board[up][left] != 0:
                    further_up = up + 1
                    further_left = left + 1
                    if further_up <= 7 and further_left <= 7 and not self.board[further_up][further_left]:
                        moves[(further_up, further_left)] = [(up, left)]
                else:
                    if up <= 7 and left <= 7:
                        moves[(up, left)] = []

                # Can we go up-right
                if self.board[up][right] != 0:
                    further_up = up + 1
                    further_right = right - 1
                    if further_up <= 7 and further_right >= 0 and not self.board[further_up][further_right]:
                        moves[(further_up, further_right)] = [(up, right)]
                else:
                    if up <= 7 and right >= 0:
                        moves[(up, right)] = []

            else:
                # Can we go up-left
                if self.board[up][left] != 0:
                    further_up = up + 1
                    further_left = left + 1
                    if further_up <= 7 and further_left <= 7 and not self.board[further_up][further_left]:
                        moves[(further_up, further_left)] = [(up, left)]
                else:
                    if up <= 7 and left <= 7:
                        moves[(up, left)] = []

                # Can we go up-right
                if self.board[up][right] != 0:
                    further_up = up + 1
                    further_right = right - 1
                    if further_up <= 7 and further_right >= 0 and not self.board[further_up][further_right]:
                        moves[(further_up, further_right)] = [(up, right)]
                else:
                    if up <= 7 and right >= 0:
                        moves[(up, right)] = []

        return moves

    def remove(self, jumped):
        for checker in jumped:
            row, col = checker
            self.board[row][col] = 0
            if checker != 0:
                if checker.color == RED:
                    self.red_remain -= 1
                elif checker.color == BLACK:
                    self.black_remain -= 1




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
