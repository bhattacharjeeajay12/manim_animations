from manim import *
import os
from pathlib import Path

FLAGS = f"-pql"

# OUT_FILE_NAME = "TARGET_1"
# config.frame_width = 4

OUT_FILE_NAME = "TARGET_2"
config.frame_width = 4
config.pixel_height = 1000
config.pixel_width = 1000

FLAG_OUTPUT_FILE = "--output_file"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        self.play(Write(NumberPlane()), run_time=4)
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
