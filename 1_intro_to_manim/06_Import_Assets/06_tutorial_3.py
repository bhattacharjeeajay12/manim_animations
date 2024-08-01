import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"


# config.background_color=WHITE

class Solution(Scene):
    def construct(self):
        svg = SVGMobject("assets\\mask_example.svg")
        # svg.height = config.frame_height - 3
        # svg.to_corner(UL, buff=1)
        svg.move_to(LEFT*2+UP*2)
        svg.set(height=3, width=3)

        #-------------------------------
        angular_svg = SVGMobject("assets\\angular-brands.svg", color=GREEN).scale(2)
        # angular_svg.next_to(svg, RIGHT)
        for submob in angular_svg:
            submob.set_color(RED)
        angular_svg.next_to(svg, RIGHT)
        angular_svg.set(height=3, width=3)

        # -------------------------------
        some_svg = SVGMobject("assets\\some_svg.svg", color=GREEN).scale(2)
        # angular_svg.next_to(svg, RIGHT)
        for submob in some_svg:
            submob.set_color(GREEN)
        some_svg.next_to(svg, DOWN)
        some_svg.set(height=3, width=3)

        #--------------------------------
        basic_svg = SVGMobject("assets\\basic_svg.svg", color=GREEN).scale(2)
        # angular_svg.next_to(svg, RIGHT)
        # for submob in basic_svg:
        #     submob.set_color(GREEN)
        basic_svg.next_to(svg, DR)
        basic_svg.set(height=3, width=3)

        self.add(svg, angular_svg, some_svg, basic_svg)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
