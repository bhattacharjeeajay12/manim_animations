import numpy as np
from manim import *
import os
from pathlib import Path
from itertools import cycle

FLAGS = f"-pqh"
SCENE = "Solution"


class Solution(Scene):
    def get_arr_mob(self, arr):
        return VGroup(*[
            self.get_cell(n)
            for n in arr
        ]).arrange(RIGHT, buff=0)

    def get_cell(self, n):
        text = Text(f"{n}")
        sq = Square(side_length=0.8)
        vg = VGroup(sq, text)
        return vg

    def construct(self):
        arr = [5, 9, 3, 1, 8, 6, 4, 2, 7]
        arr_mob = self.get_arr_mob(arr)
        arr_len = len(arr)

        self.add(arr_mob)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
