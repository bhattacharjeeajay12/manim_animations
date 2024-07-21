from manim import *
import os
from pathlib import Path
import numpy as np

FLAGS = f"-pqm"
SCENE = "Solution"

CONFIG_FLAG = f"-c"
CONFIG_FILE = "config-file-1.cfg"


def get_angle(point_1, point_2):
    dot_product = np.dot(point_1, point_2)
    magnitude1 = np.linalg.norm(point_1)
    magnitude2 = np.linalg.norm(point_2)

    # Calculate the cosine of the angle
    cos_theta = dot_product / (magnitude1 * magnitude2)

    # Clip the cosine value to the range [-1, 1] to avoid numerical errors
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Calculate the angle in radians
    angle_radians = np.arccos(cos_theta)
    return angle_radians


class Solution(Scene):
    def construct(self):
        # Define the colors and radii for the WiFi waves
        colors = [BLUE, GREEN, YELLOW, RED]
        radii = [0.5, 1.0, 1.5, 2.0]

        # Create the WiFi waves (arcs)
        wifi_waves = VGroup()
        for color, radius in zip(colors, radii):
            arc = Arc(
                radius=radius,
                start_angle=PI/4,
                angle=PI / 2,
                stroke_width=6,
                stroke_color=color,
            )

            # # option 1
            # angle_radians = get_angle(arc.get_center(), UP)
            # wifi_waves.add(arc.rotate(angle_radians, about_point=ORIGIN))

            # # option 2
            # angle_with_x_axis = arc.angle / 2  # As the arc angle is centered
            # # Calculate the rotation angle to make it perpendicular
            # rotation_angle = PI / 2 - angle_with_x_axis
            # # Rotate the arc
            # arc.rotate(rotation_angle, about_point=ORIGIN)

            wifi_waves.add(arc)

        # Create the small circle at the base
        base_circle = Dot(point=ORIGIN, color=WHITE, radius=0.1)

        # Position the WiFi waves and the base circle
        wifi_group = VGroup(wifi_waves, base_circle)
        wifi_group.move_to(ORIGIN)

        # Add everything to the scene
        self.add(wifi_group)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    # os.system(f"manim {script_name} {SCENE} {FLAGS} {CONFIG_FLAG} {CONFIG_FILE}")
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
