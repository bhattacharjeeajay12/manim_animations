import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"
flush_cache = "--flush_cache"

class Solution(Scene):
    def construct(self):
        GREEN_FLAG_COLOR = "#005940"
        ORANGE_FLAG_COLOR = "#FFA500"

        grp = Group()
        green_rect = Rectangle(color=GREEN_FLAG_COLOR, height=1, width = 6, fill_color=GREEN_FLAG_COLOR, fill_opacity=1)
        orange_rect = green_rect.copy().set(color=ORANGE_FLAG_COLOR, fill_color=ORANGE_FLAG_COLOR, fill_opacity=1)
        white_rect = green_rect.copy().set(color=WHITE, fill_color=WHITE, fill_opacity=1)
        chakra_svg = SVGMobject("assets\\Ashoka_Chakra.svg", color=GREEN).set(height=white_rect.height-0.05)

        white_rect.move_to(ORIGIN)
        green_rect.next_to(white_rect, UP, buff=0)
        orange_rect.next_to(white_rect, DOWN, buff=0)
        chakra_svg.move_to(ORIGIN)

        grp.add(white_rect, green_rect, orange_rect, chakra_svg)
        grp.scale(1.5)
        # self.add(*grp)

        self.play(
            Write(orange_rect),
            Write(green_rect),
            Write(white_rect),
        )
        self.play(Write(chakra_svg, stroke_color=BLACK, run_time=3))
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
