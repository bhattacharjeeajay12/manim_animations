import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"
flush_cache = "--flush_cache"


# class Solution(Scene):
#     def construct(self):
#         square = Square().scale(0.3)
#         pyramid_nos = 5
#         pyramid_grp = Group()
#
#         for idx in range(pyramid_nos):
#             big_group = Group()
#             for row in range(idx+1):
#                 small_group = Group()
#                 for box_count in range(idx+1-row):
#                     small_group.add(square.copy())
#                 small_group.arrange(RIGHT, buff=0)
#                 big_group.add(small_group)
#             big_group.arrange(UP, buff=0)
#             pyramid_grp.add(big_group)
#         pyramid_grp.arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
#
#         self.add(pyramid_grp)


# # Solution by DevTaoism
class Solution(Scene):

    def get_pyramid(self, n):
        return VGroup(*[
            VGroup(*[
                Square().scale(0.3)
                for _ in range(i)
            ]).arrange(RIGHT, buff=0)
            for i in range(n)
        ]).arrange(DOWN, buff=0)

    def construct(self):
        pyramids = VGroup(*[
            self.get_pyramid(i)
            for i in range(1, 7)
        ]).arrange(RIGHT, buff=0.2, aligned_edge=DOWN)
        self.add(pyramids)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
