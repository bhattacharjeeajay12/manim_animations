import numpy as np
from manim import *
import os
from pathlib import Path
import numpy as np

FLAGS = f"-pqm"
SCENE = "Solution"
flush_cache = "--flush_cache"


class Solution(Scene):
    def construct(self):
        color_list = [RED, BLUE, GREEN, YELLOW, GREEN, ORANGE, PINK, GREY]

        path = VGroup()
        first_line = Line(ORIGIN, UP / 5, stroke_width=5, color=WHITE)
        path.add(first_line)
        iterations = 3

        for i in range(iterations):
            new_path = path.copy().set_color(color_list[i])
            new_path.rotate(
                90 * DEGREES,
                about_point=path[-1].get_end() if i == 0 else path[-1].get_start()
            )
            post_path = reversed([*new_path])
            path.add(*post_path)

            # path.add(*new_path)

        path.set(height=config.frame_height - 1)
        path.move_to(ORIGIN)

        self.add(path)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
