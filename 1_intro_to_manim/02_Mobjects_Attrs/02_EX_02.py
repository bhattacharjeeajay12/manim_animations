from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"

class Solution(Scene):
    def construct(self):
        circle = Circle().to_corner(UL, buff=1)
        mobs = [circle, Square(), Star(), Triangle(), Circle()]

        for i in range(len(mobs)-1):
            mobs[i+1].next_to(mobs[i], RIGHT, aligned_edge=UP)

        self.add(*mobs)

if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
