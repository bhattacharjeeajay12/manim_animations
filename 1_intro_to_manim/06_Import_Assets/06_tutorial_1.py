import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"


class Solution(Scene):
    def construct(self):
        img = ImageMobject("assets\\test_image.png")

        img_pixel_height = len(img.pixel_array)
        img_pixel_width = len(img.pixel_array[0])

        print("img_pixel_height : ", img_pixel_height)
        print("img_pixel_width : ", img_pixel_width)

        # img.pixel_array = img.pixel_array[:int(img_pixel_height/2)]

        for row in range(img_pixel_height):
            for col in range(img_pixel_width):
                for idx in range(len(img.pixel_array[row][col])):
                    if img.pixel_array[row][col][idx] not in []:
                        img.pixel_array[row][col][idx] = img.pixel_array[row][col][idx] / 2

        # print(img.pixel_array)

        self.add(img)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
