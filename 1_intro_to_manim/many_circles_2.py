import numpy as np
from manim import *
import os
from pathlib import Path
import math

FLAGS = f"-pqm"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        fig_kwargs_1 = {"fill_opacity": 0.5, "stroke_width": 0, "color": WHITE}
        circle = Circle(**fig_kwargs_1)





        # self.add(*grp)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
