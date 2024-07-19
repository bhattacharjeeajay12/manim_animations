from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"

'''
    q: quality [l,m,h] stands for low, medium, high
'''


class Solution(Scene):
    def setup(self):
        self.add(NumberPlane())

    def construct(self):
        x_range = range(-6, 6 + 1)
        y_range = range(-3, 3 + 1)

        # using list comprehension
        dots = [
            Dot([x, y, 0])
            for x in x_range
            for y in y_range
        ]

        black_button = Rectangle(fill_opacity=0.2, color=RED)

        print(black_button.get_center(),
              black_button.get_left(),
              black_button.get_right(),
              black_button.get_top(),
              black_button.get_bottom()
              )

        self.add(*dots)
        self.add(black_button)
        self.add(black_button.copy().move_to([4,2,0]))


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
