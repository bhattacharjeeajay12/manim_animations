from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        final_objects = []

        fig_kwargs = {"fill_opacity": 1}

        circle = Circle(color=WHITE, **fig_kwargs).scale(3)
        final_objects.append(circle)

        big_triangle = Triangle(color="#2FA673", **fig_kwargs).scale(2.4)
        big_triangle.rotate(angle=PI, about_point=ORIGIN)
        final_objects.append(big_triangle)

        mid_triangle = big_triangle.copy()
        mid_triangle.scale(2/3, about_edge=UP).set_color("#2A3C4E")
        final_objects.append(mid_triangle)

        small_triangle = big_triangle.copy()
        small_triangle.scale(1/3, about_edge=UP).set_color(WHITE)
        final_objects.append(small_triangle)

        self.add(*final_objects)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
