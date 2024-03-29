# from dataclasses import dataclass
# from typing import List
# from checker import Checker
#
#
# @dataclass
# class CheckerBoard:
#     n: int
#     blacks_remain: int = None
#     whites_remain: int = None
#     board: List[List] = None
#     capture_x: int = None
#     capture_y: int = None
#
#     def __post_init__(self):
#         self.blacks_remain = self.whites_remain = self.n
#         self.board = [["" for _ in range(self.n)] for _ in range(self.n)]
#         for row in range(self.n):
#             for col in range(self.n):
#                 if col % 2 == (row+1) % 2:
#                     if row < 3:
#                         self.board[row][col] = Checker('W', (row, col), False, False)
#                     elif row > 4:
#                         self.board[row][col] = Checker('B', (row, col), False, False)
#
#     def print_board(self):
#         printing_board = [['' for _ in range(self.n)] for _ in range(self.n)]
#         for row in range(self.n):
#             for col in range(self.n):
#                 if self.board[row][col] != '':
#                     printing_board[row][col] = self.board[row][col].get_color
#
#         for row in printing_board:
#             print(row)
#
#     def get_valid_moves(self):
#         pass
#
#     def valid_move(self, source, destination):
#         # current_position = checker.get_position
#         if self.board[source[0]][source[1]] == "":
#             return False
#         if abs(destination[0] - source[0]) > 2 or\
#             abs(destination[1] - source[1]) > 2:
#             return False
#         if abs(destination[0] - source[0]) != abs(destination[1] - source[1]):
#             return False
#         if destination[0] < 0 or destination[0] >= self.n or destination[1] < 0 or destination[1] >= self.n:
#             return False
#         if self.board[destination[0]][destination[1]] != "":
#             return False
#         return True
#
#     def move_checker(self, source, destination):
#         if abs(destination[0]-source[0]) == 2 and \
#                 abs(destination[1] - source[1]) == 2:
#             if self.check_capture(source, destination):
#                 if self.board[self.capture_x][self.capture_y].get_color == "W":
#                     self.whites_remain -= 1
#                 else:
#                     self.blacks_remain -= 1
#                 self.board[self.capture_x][self.capture_y].set_captured(True)
#                 self.board[self.capture_x][self.capture_y] = ""
#
#         self.board[source[0]][source[1]].set_position(destination)
#         self.board[destination[0]][destination[1]] = self.board[source[0]][source[1]]
#         self.board[source[0]][source[1]] = ""
#
#     def check_capture(self, source, destination):
#         if destination[0] > source[0]:
#             self.capture_x = destination[0] - 1
#         else:
#             self.capture_x = destination[0] + 1
#         if destination[1] > source[1]:
#             self.capture_y = destination[1] - 1
#         else:
#             self.capture_y = destination[1] + 1
#
#         if self.board[self.capture_x][self.capture_y] != "":
#             return True
#         else:
#             return False
#
#     def check_end_game(self):
#         if self.whites_remain == 0:
#             print('Black Wins')
#         elif self.blacks_remain == 0:
#             print('White Wins')
#
#     def simulate_move(self, source, destination):
#         if self.valid_move(source, destination):
#             self.check_end_game()
#             self.move_checker(source, destination)
