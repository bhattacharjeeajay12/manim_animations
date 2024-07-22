import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"


class MyScene(Scene):
    def setup(self):
        self.axes = Axes(
            x_range=[0, 1.2, 1],
            y_range=[0, 1.2, 1],
            x_length=5,
            y_length=5,
            axis_config={
                "include_numbers": False,  # Exclude numbers at each tick
                "numbers_to_include": [1],  # Only include numbers 0 and 1
                "include_ticks": True
            },
            # Additional configurations to customize axes appearance
            x_axis_config={
                "label_direction": DOWN,  # Labels facing down for x-axis
            },
            y_axis_config={
                "label_direction": LEFT,  # Labels facing left for y-axis
            }
        )

        self.axes.move_to(LEFT * 3)
        # Add labels for the axes
        x_label = Text("% run time", font_size=24)
        y_label = Text("% Animation", font_size=24).rotate(PI / 2)

        # Position the labels at the middle of the axes
        x_label.next_to(self.axes.c2p(0.5, 0), DOWN)
        y_label.next_to(self.axes.c2p(0, 0.5), LEFT)

        self.add(self.axes, x_label, y_label)


class Solution(MyScene):
    def construct(self):

        rate_func_list = [smooth, linear, exponential_decay, there_and_back]
        color_list = [RED, BLUE, GREEN, YELLOW]
        label_group = Group(*[Text(rf.__name__, color=colour, font_size=24) for rf, colour in zip(rate_func_list, color_list)])
        label_group.arrange(DOWN, aligned_edge=LEFT)
        label_group.next_to(self.axes)
        plots = [self.axes.plot(rf, x_range=[0, 1, 0.01], color=colour) for rf, colour in
                 zip(rate_func_list, color_list)]

        vt = ValueTracker(-5)

        f2 = always_redraw(lambda: self.axes.plot(lambda x: smooth, color=RED, x_range=[0, vt.get_value()]))
        # f2 = always_redraw(lambda: ax.plot(lambda x: (1 / 2) * x + 1, color=YELLOW, x_range=[-5, vt.get_value()]))

        self.add(*plots, label_group)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
