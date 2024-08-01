import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"
flush_cache = "--flush_cache"

# config.background_color=WHITE
# from manimlib.scene.interactive_scene import InteractiveScene
# class Solution(InteractiveScene):
class Solution(Scene):
    def construct(self):
        # sq = Square(fill_opacity=1)
        # self.play(FadeToColor(sq, RED, run_time=2))
        # self.wait()
        # self.add_sound("assets\\beep-04.wav")
        # self.play(FadeToColor(sq, BLUE, run_time=1))
        # self.play(FadeToColor(sq, GREEN, run_time=3))
        # self.wait(2)
        # self.play(FadeToColor(sq, YELLOW, run_time=2))
        # self.wait()

        # for i in range(5):
        #     t = Text(f"{i + 1}")
        #     t.set(height=config.frame_height - 2)
        #
        #     if i != 4:
        #         self.add(t)
        #         # "gain" is the amplification of the sound
        #         self.add_sound("assets/count.wav", gain=3)
        #     else:
        #         self.add(t)
        #         self.add_sound("assets/stop.wav", gain=3)
        #     self.wait(1)
        #     self.remove(t)

        sq = Square(fill_opacity=1)

        self.play(FadeToColor(sq, RED, run_time=2))
        self.wait()
        self.add_sound("assets\\count.wav")
        self.play(FadeToColor(sq, BLUE, run_time=1))
        self.play(FadeToColor(sq, GREEN, run_time=3))
        self.wait(2)
        self.play(FadeToColor(sq, YELLOW, run_time=2))
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
