from manim import *
import os
from pathlib import Path
import numpy as np
import math

FLAGS = f"-pqm"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        white_button = Rectangle(width=0.7, height=3, fill_opacity=1, color=WHITE, stroke_color=BLUE_A, stroke_width=0.1)
        black_button = Rectangle(width=0.5, height=2, fill_opacity=1, color=GREY_BROWN)
        piano_header = Rectangle(height=0.2, fill_opacity=1, color=GREY)

        n_white_buttons = 16
        white_buttons = VGroup()
        black_buttons = VGroup()
        all_buttons = VGroup()

        for i in range(n_white_buttons):
            wb = white_button.copy()
            if i == 0:
                wb.to_corner(UL, buff=1)
            white_buttons.add(wb)

        for i in range(len(white_buttons) - 1):
            white_buttons[i + 1].next_to(white_buttons[i], RIGHT, aligned_edge=UP, buff=0.1)

        for i in range(len(white_buttons) - 1):
            if (i + 1) % 3 != 0:
                bb = black_button.copy()
                mean_x_position = (white_buttons[i].get_center()[0] + white_buttons[i+1].get_center()[0])/2

                bb_y_diff = math.sqrt((bb.get_top()[0] - bb.get_bottom()[0]) ** 2 + (bb.get_top()[1] - bb.get_bottom()[1]) ** 2)
                wb_top_y = (white_buttons[i].get_top()[1] - bb_y_diff/2)

                desired_wb_pos = np.array([mean_x_position, wb_top_y, 0])
                bb.move_to(desired_wb_pos)
                black_buttons.add(bb)

        all_buttons.add(*[white_buttons, black_buttons])
        piano_header.set(width=all_buttons.width)
        piano_header.next_to(all_buttons, UP, buff=0)

        self.add(*all_buttons)
        self.add(piano_header)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
