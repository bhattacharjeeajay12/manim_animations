import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"


class Example(Scene):

    def construct(self):
        source = MathTex("\\sqrt{\\frac{1}{8}}")[0]  # source = SingleStringMathTex("\\sqrt{\\frac{1}{8}}")
        target = MathTex("\\frac{1}{2\\sqrt{2}}")[0]  #target = SingleStringMathTex("\\frac{1}{2\\sqrt{2}}")

        VGroup(source, target).scale(4)
        self.add(source)
        # VGroup(source, target).scale(4).arrange(RIGHT)
        # self.add(source, target)

        transform_index = [
            [0, 1, 2, 3, 4],
            # | | | | | |    Note that we repeat the index 4 twice,
            # v v v v v v     since the "8" is going to transform
            [3, 4, 0, 1, 2]  # into two different symbols.
        ]

        transforms = [
            ReplacementTransform(source[i], target[j])
            for i, j in zip(transform_index[0], transform_index[1])
        ]
        transforms.append(ReplacementTransform(source[4].copy(), target[5]))

        self.play(*transforms)
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
