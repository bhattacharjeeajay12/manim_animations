from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"

'''
    q: quality [l,m,h] stands for low, medium, high
'''

class Solution(Scene):
    def setup(self):
        self.add(NumberPlane())

    def construct(self):
        x_range = range(-6, 6+1)
        y_range = range(-3, 3 + 1)

        # using list comprehension
        dots = [
            Dot([x, y, 0])
            for x in x_range
            for y in y_range
        ]
        self.add(*dots)

if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
