import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqh"
SCENE = "Solution"

class Solution(Scene):
    def construct(self):
        image_data = [
            [157, 153, 174, 158, 150, 152, 129, 151, 172, 161, 155, 156],
            [155, 182, 163, 74, 75, 62, 33, 17, 110, 210, 180, 154],
            [180, 180, 50, 14, 34, 6, 10, 33, 48, 106, 159, 181],
            [206, 109, 5, 124, 131, 111, 120, 204, 166, 15, 56, 180],
            [194, 64, 193, 251, 237, 239, 289, 228, 227, 87, 71, 201],
            [172, 106, 207, 233, 233, 214, 220, 239, 228, 38, 74, 206],
            [138, 88, 179, 209, 186, 215, 211, 158, 139, 75, 20, 169],
            [189, 37, 165, 84, 10, 168, 134, 11, 31, 62, 22, 148],
            [199, 168, 191, 193, 158, 227, 187, 143, 182, 106, 36, 190],
            [206, 174, 155, 252, 236, 231, 149, 178, 228, 43, 95, 234],
            [190, 216, 116, 149, 236, 187, 85, 150, 79, 38, 218, 241],
            [190, 224, 147, 108, 227, 210, 127, 102, 36, 101, 255, 224],
            [190, 214, 173, 66, 103, 143, 95, 50, 2, 109, 249, 215],
            [187, 196, 235, 75, 1, 81, 49, 0, 6, 127, 255, 211],
            [183, 202, 237, 145, 0, 0, 12, 108, 200, 138, 243, 236],
            [195, 206, 123, 207, 177, 121, 123, 200, 175, 13, 96, 218],
        ]

        text_list_ = [Text("cubic (default paramenter)", font_size=24), Text("nearest", font_size=24)]

        image_unit8 = np.uint8(image_data)
        img = ImageMobject(image_unit8)
        img.height = config.frame_height - 2
        img.to_edge(LEFT, buff=2)
        img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["cubic"])

        img_pixeled = img.copy()
        img_pixeled.to_edge(RIGHT, buff=2)
        img_pixeled.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])

        img_lists = [img, img_pixeled]
        text_list = [text_obj.next_to(img_obj, UP) for text_obj, img_obj in zip(text_list_, img_lists)]

        self.add(*img_lists, *text_list)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
