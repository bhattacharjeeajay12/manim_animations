import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"


class Solution(Scene):

    def construct(self):
        up_tex = MathTex(
            # 0         1       2   3    4
            "\\neg", "\\forall", "x", ":", "P(x)",
        ).scale(2)
        down_tex = MathTex(
            #    0      1   2      3     4
            "\\exists", "x", ":", "\\neg", "P(x)"
        ).scale(2)

        VGroup(up_tex, down_tex).arrange(DOWN)
        self.play(
            Write(up_tex)
        )
        self.wait()

        steps = [
            # Step 1
            [[2, 3, 4],
             [1, 2, 4]],
            # Step 2
            [[0],
             [3]],
            # Step 3
            [[1],
             [0]],
        ]

        for step in steps:
            base, target = step
            self.play(*[
                ReplacementTransform(up_tex[i].copy(), down_tex[j], run_time=3)
                for i, j in zip(base, target)
            ])
            self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
