import numpy as np
from manim import *
import os
from pathlib import Path
import math

FLAGS = f"-pqm"
SCENE = "Solution"


def get_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


class Solution(Scene):
    def construct(self):

        square = Square(side_length=1.5)
        n_rows = 4
        n_square = 4

        group = VGroup()
        for i in range(n_rows * n_square):
            square = square.copy()
            group.add(square)

        group.arrange_in_grid(n_rows, n_square)
        dist_between_square = get_distance(group[0].get_right(), group[1].get_left())

        self.add(*group)
        for row in range(n_rows):
            for col in range(n_square):
                square_index = row * n_square + col

                lrtp = [group[square_index].get_left(), group[square_index].get_right(), group[square_index].get_top(),
                        group[square_index].get_bottom()]
                directions = [LEFT, RIGHT, UP, DOWN]
                for start_point, direction in zip(lrtp, directions):
                    end_point = start_point + direction * dist_between_square
                    line = Line(start_point, end_point)
                    self.add(line)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
