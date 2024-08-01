import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"
flush_cache = "--flush_cache"

config.pixel_height = 576
config.pixel_width = 1707

# config.pixel_height = 1440
# config.pixel_width = 2560

class Solution(Scene):
    def construct(self):
        buff = 0.2
        combined_lines = VMobject()
        combined_lines.set_points_as_corners([LEFT + [0, buff, 0], UL, UP - [buff, 0, 0]])
        combined_lines.set_stroke(width=10)

        line_red = combined_lines.copy().set_color(RED)
        line_green = combined_lines.copy().set_color(GREEN).rotate(-PI / 2, about_point=ORIGIN)
        line_blue_1 = combined_lines.copy().set_color(BLUE).rotate(PI / 2, about_point=ORIGIN)
        line_blue_2 = combined_lines.copy().set_color(BLUE).rotate(2 * PI / 2, about_point=ORIGIN)

        line_grp = Group(line_red, line_green, line_blue_1, line_blue_2)
        line_grp.scale(0.5)

        tex_m, tex_i = Text("M", font_size=25, color=YELLOW), Text("I", font_size=25, color=YELLOW)
        tex_i.next_to(tex_m, RIGHT, aligned_edge=RIGHT, buff=0.2)
        text_grp = Group(tex_m, tex_i)
        text_grp.move_to(ORIGIN)

        company_name = Text("MATH IMAGERY", font_size=12, color=YELLOW)
        company_name.next_to(line_grp, DOWN, buff=0.2)

        final_grp = Group(line_grp, text_grp, company_name)

        final_grp.scale(1.3)  # Adjust the scale as needed
        final_grp.move_to(ORIGIN)  # Center the logo on the screen

        final_grp.to_corner(LEFT)

        n_circle = 80

        all_object = Group()
        circle = Circle(radius=1.5).move_to(2 * RIGHT)
        all_object.add(circle)
        for i in range(n_circle):
            circle = circle.copy().rotate(about_point=ORIGIN, angle=PI / 30)
            all_object.add(circle)

        # all_object.to_corner(RIGHT)
        all_object.to_corner(RIGHT, buff=-4)

        banner = Group(final_grp, all_object)
        banner.scale(.5)

        self.add(banner)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
