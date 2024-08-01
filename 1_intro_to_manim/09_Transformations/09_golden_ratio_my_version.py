import numpy as np
from manim import *
import os
from pathlib import Path
from itertools import cycle

FLAGS = f"-pqh"
SCENE = "Solution"


def get_arc(down_left_corner, upper_right_corner, center):
    radius = np.linalg.norm(upper_right_corner - center)

    # Calculate start and end angles for the arc
    start_angle = np.arctan2(down_left_corner[1] - center[1], down_left_corner[0] - center[0])
    end_angle = np.arctan2(upper_right_corner[1] - center[1], upper_right_corner[0] - center[0])
    print("start_angle : ", start_angle)
    print("end_angle : ", end_angle)

    angle = end_angle - start_angle
    print("angle : ", angle)
    if angle > PI:
        print("True")
        angle -= 2 * PI
        print("angle : ", angle)

    print("-" * 10)
    # Draw the arc
    return Arc(
        start_angle=start_angle,
        angle=angle,
        radius=radius,
        color=BLUE,
        arc_center=center,
        stroke_width=2
    )


class Solution(Scene):

    def construct(self):
        print("PI : ", PI)
        phi = (1 + np.sqrt(5)) / 2
        phi_inv = 1 / phi
        square_list = []

        next_to = cycle([RIGHT, DOWN, LEFT, UP])
        aligned_edge = cycle([UP, RIGHT, DOWN, LEFT])
        corners = cycle([UR, DR, DL, UL])
        centers = cycle([DR, DL, UL, UR])

        sq = Square(stroke_width=2).scale(3).shift(LEFT)
        self.add(sq)
        square_list.append(sq)
        end_corner = sq.get_corner(next(corners))
        arcs = get_arc(sq.get_corner(DL), end_corner, sq.get_corner(next(centers)))

        for idx in range(1, 5):
            last_sq = sq.copy()
            sq = sq.copy().scale(phi_inv).next_to(sq, next(next_to), aligned_edge=next(aligned_edge), buff=0)
            square_list.append(sq)
            start_corner = end_corner
            end_corner = sq.get_corner(next(corners))
            arcs.append_vectorized_mobject(get_arc(start_corner, end_corner, sq.get_corner(next(centers))))

            self.play(
                TransformFromCopy(last_sq, sq),
                run_time=2
            )
            self.wait(0.5)

        arc_animations = [Create(arc) for arc in arcs]
        self.play(AnimationGroup(*arc_animations, run_time=2))


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
