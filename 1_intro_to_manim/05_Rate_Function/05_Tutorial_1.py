import numpy as np
from manim import *
import os
from pathlib import Path
import numpy as np

FLAGS = f"-pqm"
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
        color_list = [RED, GREEN, BLUE, WHITE]
        dot_list = []
        line_list = []
        text_list = []
        labels = ["smooth", "linear", "exponential_decay", "there_and_back"]
        rate_function_list = [smooth, linear, exponential_decay, there_and_back]
        start_position = np.array([-5, -1, 0])
        end_position = np.array([1, -1, 0])

        for idx, (color, text) in enumerate(zip(color_list, labels)):
            text = Text(text, color=color, font_size=35)
            if idx == 0:
                dot = Dot().set(color=color).move_to(start_position)
                dot_list.append(dot)

                line = Line(start_position, end_position, color=color)
                line_list.append(line)
            else:
                dot = dot.copy().set(color=color).shift(UP)
                dot_list.append(dot)

                line = line.copy().set(color=color).shift(UP)
                line_list.append(line)

            text.next_to(line, RIGHT, buff=0.2)
            text_list.append(text)

        self.add(*dot_list, *line_list, *text_list)

        self.play(
            *[dot.animate(rate_func=rate_function, run_time=6).shift(RIGHT*6) for dot, rate_function in zip(dot_list, rate_function_list)]
        )


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
