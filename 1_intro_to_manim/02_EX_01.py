from manim import *
import os

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
    os.system(r"manim --disable_caching -v WARNING 02_EX_01.py Solution -qm ")