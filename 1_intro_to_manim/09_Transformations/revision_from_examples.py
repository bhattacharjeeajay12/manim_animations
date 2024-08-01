import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"


class Solution(Scene):
    # def construct(self):
    #     target = Circle()
    #     # target = VGroup(*[Circle() for _ in range(5)]).arrange(RIGHT)
    #     base = VGroup(Triangle(), Square(), Star(), RegularPolygon(5)).arrange(RIGHT)
    #     group = VGroup(base, target).arrange(DOWN)
    #
    #     self.add(base)
    #     self.wait()
    #     self.play(TransformFromCopy(base, target, run_time=4))

    # def construct(self):
    #     c = Circle().scale(2)
    #     img = ImageMobject(
    #         np.uint8([[0, 100, 30, 200],
    #                   [255, 0, 5, 33]]
    #                  )).set(height=4)
    #
    #     Group(c, img).arrange(RIGHT, buff=1)
    #
    #     self.add(c, img)
    #     print(f"Before transform: Scene.mobjects: {self.mobjects}")
    #     self.wait(3)
    #     self.play(
    #         FadeTransform(c, img),
    #         run_time=4
    #     )
    #     self.wait(2)
    #     print(f"Post transform: Scene.mobjects: {self.mobjects}")

    def construct(self):
        t1 = MathTex("e^", "\\frac{-it\\pi}{\\omega}")
        t2 = MathTex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1, t2) \
            .scale(3) \
            .arrange(DOWN, buff=2)

        self.add(t1, t2.copy().fade(0.8))
        self.wait(0.3)
        self.play(
            FadeTransform(t1[-1].copy(), t2[0]),
            run_time=4
        )
        self.wait()


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
