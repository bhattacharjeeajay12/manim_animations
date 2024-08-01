import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"
flush_cache = "--flush_cache"

class Solution(Scene):
    def construct(self):
        black_square = Square(fill_opacity=1, fill_color=BLACK, stroke_width=1).set(height=0.5)
        white_square = Square(fill_opacity=1, fill_color=WHITE, stroke_width=1).set(height=0.5)

        row_even = Group(*[white_square.copy() if i % 2 == 0 else black_square.copy() for i in range(0, 8)])
        row_odd = Group(*[black_square.copy() if i % 2 == 0 else white_square.copy() for i in range(0, 8)])

        row_even.arrange(RIGHT, buff=0)
        row_odd.arrange(RIGHT, buff=0)

        chess_board = Group(*[row_even.copy() if i % 2 == 0 else row_odd.copy() for i in range(0, 8)])
        chess_board.arrange(DOWN, buff=0)
        chess_board.scale(1.5)

        self.add(*chess_board)

# Solution by DecTaoism
# class Solution(Scene):
#     def construct(self):
#         from itertools import cycle
#         colors = cycle([WHITE, BLACK])
#         LENGTH = 8
#         board = VGroup(*[
#             VGroup(*[
#                 Square(fill_opacity=1, fill_color=next(colors), stroke_width=1).set(height=0.5)
#                 for _ in range(LENGTH)
#             ]).arrange(RIGHT if j % 2 == 0 else LEFT, buff=0)
#             for j in range(LENGTH)
#         ]).arrange(DOWN, buff=0)
#         board.scale(1.3)
#
#         self.add(board)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
