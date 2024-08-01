import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"
flush_cache = "--flush_cache"


# config.pixel_height = 576
# config.pixel_width = 1707

# config.pixel_height = 1440
# config.pixel_width = 2560

class Solution(Scene):
    def construct(self):
        tag = Text("Applied Math in Visuals", font_size=30, color=YELLOW_A, stroke_color=RED, stroke_width=0.7)

        n_circle = 120

        all_object = Group()
        circle = Circle(radius=3, stroke_width=1, stroke_opacity=0.3).move_to(RIGHT * 3)
        # all_object.add(circle)
        for i in range(n_circle):
            circle = circle.copy().rotate(about_point=ORIGIN, angle=PI / 30)
            all_object.add(circle)

        # all_object.to_corner(RIGHT, buff=-4)
        all_object.move_to(ORIGIN)
        tag.move_to(ORIGIN)
        banner = Group(all_object, tag)

        self.add(banner)


class MyTex(Tex):
    def __init__(self, *args, j_width=4, **kwargs):
        # super().__init__(*args, tex_environment="\\begin{tabular}{p{%s cm}}"%j_width, **kwargs)
        tex_env = "\\begin{tabular}{p{%s cm}}" % j_width
        super().__init__(*args, tex_environment=tex_env, **kwargs)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
