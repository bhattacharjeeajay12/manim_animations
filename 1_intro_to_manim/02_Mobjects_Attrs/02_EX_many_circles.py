from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        n_circle = 80

        all_object = []
        circle = Circle(radius=1.5).move_to(2*RIGHT)
        all_object.append(circle)
        for i in range(n_circle):
            circle = circle.copy().rotate(about_point=ORIGIN, angle=PI/30)
            all_object.append(circle)

        self.add(*all_object)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
