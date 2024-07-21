from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"

class Solution(Scene):
    def construct(self):
        r = Rectangle()
        self.add(r)

        directions = [r.get_center(), r.get_top(), r.get_corner(UR), r.get_right(), r.get_corner(DR), r.get_bottom(), r.get_corner(DL), r.get_left(), r.get_corner(UL)]
        labels = ["C", "T", "UR", "R", "DR", "B", "DL", "L", "UL"]

        for d, l in zip(directions, labels):
            t = Text(f"{l}", color=YELLOW)
            t.move_to(d)
            self.add(t)

if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
