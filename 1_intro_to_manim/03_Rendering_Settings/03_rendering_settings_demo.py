from manim import *
import os
from pathlib import Path
import numpy as np

FLAGS = f"-qm"
SCENE = "Solution"
CONFIG_FLAG = f"-c"
CONFIG_FILE = "../03_Rendering_Settings/config-file-1.cfg"


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
                start_angle=PI / 4,
                angle=PI / 2,
                stroke_width=6,
                stroke_color=color,
            )

            wifi_waves.add(arc)

        # Create the small circle at the base
        base_circle = Dot(point=ORIGIN, color=GREY, radius=0.1)

        # Position the WiFi waves and the base circle
        wifi_group = VGroup(wifi_waves, base_circle)
        wifi_group.move_to(ORIGIN)

        # Add everything to the scene
        self.add(wifi_group)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {CONFIG_FLAG} {CONFIG_FILE}")
    # os.system(f"manim {script_name} {SCENE} {FLAGS}")
