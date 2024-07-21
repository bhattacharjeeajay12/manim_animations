from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"


class MyScene(Scene):
    def setup(self):
        self.number_plane = NumberPlane(axis_config={"include_numbers": True})
        self.add(self.number_plane)


class Solution(MyScene):
    def construct(self):
        grp = [Square(), Circle(), Star(), Triangle()]
        corner_vectors = [UR, UL, DL, DR]
        for mob, cv in zip(grp, corner_vectors):
            mob.to_corner(cv)
        self.add(*grp)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
