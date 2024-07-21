from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        fig_kwargs = {"color": RED, "fill_opacity": 0.8, "stroke_width": 0}
        left_circle = Circle(**fig_kwargs).set(height=4)
        right_circle = left_circle.copy()
        square = Square(**fig_kwargs).set(height=4)

        left_circle.shift(LEFT * 2)
        right_circle.shift(RIGHT * 2)

        pivot_kwargs_1 = {"angle": -PI / 4, "about_point": square.get_center()}
        pivot_kwargs_2 = {"angle": PI / 4, "about_point": square.get_center()}

        square.rotate(**pivot_kwargs_1)
        left_circle.rotate(**pivot_kwargs_1)

        pivot_kwargs_2 = {"angle": PI / 4, "about_point": square.get_center()}
        right_circle.rotate(**pivot_kwargs_2)
        objects = [square, right_circle, left_circle]

        self.add(*objects)
        # self.add(square,left_circle,right_circle)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
