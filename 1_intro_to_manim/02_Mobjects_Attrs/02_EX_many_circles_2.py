import numpy as np
from manim import *
import os
from pathlib import Path
import math

FLAGS = f"-pqm"
SCENE = "Solution"

class Solution(Scene):
    def construct(self):
        group = VGroup()

        fig_kwargs_1 = {"fill_opacity": 0.5, "stroke_width": 0, "radius": 1.8}
        colours = [RED, GREEN, YELLOW, BLUE]

        big_circles = []
        for i, MColor in enumerate(colours):
            circle = Circle(**fig_kwargs_1).move_to(LEFT * fig_kwargs_1["radius"]).set(color=MColor)
            circle.rotate(i*-PI/2, about_point=ORIGIN)
            big_circles.append(circle)

        small_circles = [circle.copy().set(height=fig_kwargs_1["radius"] / 1.2) for circle in big_circles]

        self.add(*big_circles, *small_circles)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
