# from dataclasses import dataclass
# from typing import Tuple
#
#
# @dataclass
# class Checker:
#     color: str
#     position: Tuple[int, int]
#     captured: bool = False
#     isKing: bool = False
#
#     @property
#     def get_color(self):
#         return self.color
#
#     @property
#     def get_position(self):
#         return self.position
#
#     def set_position(self, new_position):
#         self.position = new_position
#
#     @property
#     def is_captured(self):
#         return self.captured
#
#     def set_captured(self, if_captured):
#         self.captured = if_captured
#
#     @property
#     def is_king(self):
#         return self.isKing
#
#     def set_king(self, if_king):
#         self.isKing = if_king