import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"


class MyScene(Scene):
    def setup(self):
        self.axes_group = Group()
        self.axes_count = 8

        for idx in range(self.axes_count):
            self.axes = Axes(
                x_range=[-0.2, 1.3, 1],
                y_range=[-0.2, 1.3, 1],
                x_length=2.5,
                y_length=2.5,
                axis_config={
                    "include_numbers": False,  # Exclude numbers at each tick
                    # "numbers_to_include": [1],  # Only include numbers 0 and 1
                    "include_ticks": True,
                    "tip_width": 0.2,
                    "tip_height": 0.2
                },
                # Additional configurations to customize axes appearance
                x_axis_config={
                    "label_direction": DOWN,  # Labels facing down for x-axis
                },
                y_axis_config={
                    "label_direction": LEFT,  # Labels facing left for y-axis
                }
            )
            self.axes_group.add(self.axes)
            self.axes_group.arrange_in_grid(rows=2, cols=4, buff=1)

        self.add(*self.axes_group)


class Solution(MyScene):
    def construct(self):
        rate_func_list = [smooth, linear, rush_into, rush_from, slow_into, double_smooth, there_and_back,
                          exponential_decay]
        label_group = Group(*[Text(rf.__name__, font_size=18).next_to(axs, DOWN, buff=0) for rf, axs in
                              zip(rate_func_list, self.axes_group)])
        plots = [axs.plot(rf, x_range=[0, 1, 0.01], color=YELLOW) for rf, axs in zip(rate_func_list, self.axes_group)]

        self.add(*plots, *label_group)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
