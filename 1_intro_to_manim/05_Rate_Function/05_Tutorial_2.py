import numpy as np
from manim import *
import os
from pathlib import Path
import numpy as np
import copy

FLAGS = f"-pqh"
SCENE = "Solution"


class MyScene(Scene):
    def setup(self):
        self.number_plane = NumberPlane(background_line_style={
            "stroke_opacity": 0.3
        },
            axis_config={"stroke_opacity": 0}
        )
        self.add(self.number_plane)


class Solution(MyScene):
    def construct(self):
        colors = [RED, BLUE, GREEN, WHITE]
        top_group = Group()

        labels = ["smooth", "linear", "exponential_decay", "there_and_back"]
        rate_funcs = [smooth, linear, exponential_decay, there_and_back]

        for idx, (colour, text, rate_func) in enumerate(zip(colors, labels, rate_funcs)):
            small_group = Group()
            text_1 = Text(text, color=colour, font_size=25)
            circle = Circle(color=colour)
            text_1.next_to(circle, DOWN)

            small_group.add(circle, text_1)
            top_group.add(small_group)

        top_group.arrange(RIGHT, buff=1)
        top_group.to_corner(UL)

        bottom_group = top_group.copy()
        bottom_group.to_corner(DOWN)

        self.add(*top_group, *bottom_group)
        self.play(
            *[Create(circle[0], rate_func=rf, run_time=6) for circle, rf in
              zip(top_group, rate_funcs)],
            *[GrowFromCenter(circle[0], rate_func=rf, run_time=6) for circle, rf in
              zip(bottom_group, rate_funcs)]
        )


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
