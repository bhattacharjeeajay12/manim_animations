from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        final_objects = []

        fig_kwargs_1 = {"fill_opacity": 1, "stroke_width": 0, "color": WHITE}
        fig_kwargs_2 = {"fill_opacity": 1, "stroke_width": 0, "color": BLACK}

        big_circle = Circle(color=WHITE).set(height=6)

        semi_circle = VMobject(**fig_kwargs_1).set_points(
            big_circle.points[: int(len(big_circle.points) / 2)]
        )
        semi_circle.rotate(angle=PI / 2, about_point=ORIGIN)
        final_objects.append(semi_circle)

        up_black_circle = Circle(**fig_kwargs_2).set(height=big_circle.height / 2)
        up_black_circle.move_to(UP * 1.5)
        final_objects.append(up_black_circle)

        down_white_circle = Circle(**fig_kwargs_1).set(height=big_circle.height / 2)
        down_white_circle.move_to(DOWN * 1.5)
        final_objects.append(down_white_circle)

        small_black_circle = Circle(**fig_kwargs_2).set(height=up_black_circle.height / 3)
        small_black_circle.move_to(DOWN * big_circle.height / 4)
        final_objects.append(small_black_circle)

        small_white_circle = Circle(**fig_kwargs_1).set(height=up_black_circle.height / 3)
        small_white_circle.move_to(UP * big_circle.height / 4)
        final_objects.append(small_white_circle)

        final_objects.append(big_circle)
        self.add(*final_objects)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
