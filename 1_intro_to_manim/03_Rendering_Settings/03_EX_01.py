from manim import *
import os
from pathlib import Path

# nums = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4,   5,  6]
# cont = [ 0,  1,  2,  3,  4,  5, 6, 7, 8, 9, 10, 11, 12]

FLAGS = f"-pql"

FLAGS_SCENE_NO, SCENE_NO, CONFIG_FLAG, OUT_FILE_NAME, FLAG_SAVE_LAST_FRAME = f"-n", "0,5", f"-c", "TARGET_1", ""
# FLAGS_SCENE_NO, SCENE_NO, CONFIG_FLAG, OUT_FILE_NAME, FLAG_SAVE_LAST_FRAME = f"-n", "4,5", f"-c", "TARGET_2", f"-s"
# FLAGS_SCENE_NO, SCENE_NO, CONFIG_FLAG, OUT_FILE_NAME, FLAG_SAVE_LAST_FRAME = f"-n", "3,12", f"-c", "TARGET_3", ""
# FLAGS_SCENE_NO, SCENE_NO, CONFIG_FLAG, OUT_FILE_NAME, FLAG_SAVE_LAST_FRAME = f"-n", "13", f"-c", "TARGET_4", ""

SCENE = "Solution"
CONFIG_FILE = "../03_Rendering_Settings/config-file-2.cfg"
FLAG_OUTPUT_FILE = "--output_file"


class Solution(Scene):
    def construct(self):
        # We will learn this in deep in
        # Chapter 7
        texts = VGroup(*[
            Text(f"{i}")
            for i in range(-6, 7)
        ]).arrange(RIGHT, buff=1)
        texts.set(width=config.frame_width - 1)
        # Learn to use `enumerate` func
        for t in texts:
            # Use print("...") to help you
            self.play(GrowFromCenter(t))
            self.wait()
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"

    os.system(
        f"manim {script_name} {SCENE} {CONFIG_FLAG} {CONFIG_FILE} {FLAGS_SCENE_NO} {SCENE_NO} {FLAG_OUTPUT_FILE} {OUT_FILE_NAME} {FLAGS} {FLAG_SAVE_LAST_FRAME}")
    # os.system(f"manim {script_name} {SCENE} {FLAGS} {FLAG_OUTPUT_FILE} {OUT_FILE_NAME}")
